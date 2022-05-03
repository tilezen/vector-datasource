-- This config example file is released into the Public Domain.
-- inspect = require('inspect')
-- This configuration for the flex output tries to be compatible with the
-- original pgsql C transform output. There might be some corner cases but
-- it should do exactly the same in almost all cases.
-- The output projection used (3857, web mercator is the default). Set this
-- to 4326 if you were using the -l|--latlong option or to the EPSG
-- code you were using on the -E|-proj option.
local srid = 3857

-- Set this to true if you were using option -K|--keep-coastlines.
local keep_coastlines = false

-- Set this to the table name prefix (what used to be option -p|--prefix).
local prefix = 'planet_osm'

-- Set this to true if multipolygons should be written as multipolygons into
-- db (what used to be option -G|--multi-geometry).
local multi_geometry = false

-- Set this to true if you want an hstore column (what used to be option
-- -k|--hstore). Can not be true if "hstore_all" is true.
local hstore = false

-- Set this to true if you want all tags in an hstore column (what used to
-- be option -j|--hstore-all). Can not be true if "hstore" is true.
local hstore_all = true

-- Only keep objects that have a value in one of the non-hstore columns
-- (normal action with --hstore is to keep all objects). Equivalent to
-- what used to be set through option --hstore-match-only.
local hstore_match_only = false

-- Set this to add an additional hstore (key/value) column containing all tags
-- that start with the specified string, eg "name:". Will produce an extra
-- hstore column that contains all "name:xx" tags. Equivalent to what used to
-- be set through option -z|--hstore-column. Unlike the -z option which can
-- be specified multiple time, this does only support a single additional
-- hstore column.
local hstore_column = nil

-- There is some very old specialized handling of route relations in osm2pgsql,
-- which you probably don't need. This is disabled here, but you can enable
-- it by setting this to true. If you don't understand this, leave it alone.
local enable_legacy_route_processing = false

-- ---------------------------------------------------------------------------

if hstore and hstore_all then
    error("hstore and hstore_all can't be both true")
end

-- Used for splitting up long linestrings
if srid == 4326 then
    max_length = 1
else
    max_length = 100000
end

-- Ways with any of the following keys will be treated as polygon
local polygon_keys = {
    'aeroway',
    'amenity',
    'building',
    'harbour',
    'historic',
    'landuse',
    'leisure',
    'man_made',
    'military',
    'natural',
    'office',
    'place',
    'power',
    'public_transport',
    'shop',
    'sport',
    'tourism',
    'water',
    'waterway',
    'wetland',
    'abandoned:aeroway',
    'abandoned:amenity',
    'abandoned:building',
    'abandoned:landuse',
    'abandoned:power',
    'area:highway'
}

-- Objects without any of the following keys will be deleted
local generic_keys = {
    'access',
    'addr:housename',
    'addr:housenumber',
    'addr:interpolation',
    'admin_level',
    'aerialway',
    'aeroway',
    'amenity',
    'area',
    'barrier',
    'bicycle',
    'boundary',
    'brand',
    'bridge',
    'building',
    'capital',
    'construction',
    'covered',
    'culvert',
    'cutting',
    'denomination',
    'disused',
    'ele',
    'embankment',
    'foot',
    'generation:source',
    'harbour',
    'highway',
    'historic',
    'hours',
    'intermittent',
    'junction',
    'landuse',
    'layer',
    'leisure',
    'lock',
    'man_made',
    'military',
    'motorcar',
    'name',
    'natural',
    'office',
    'oneway',
    'operator',
    'place',
    'population',
    'power',
    'power_source',
    'public_transport',
    'railway',
    'ref',
    'religion',
    'route',
    'service',
    'shop',
    'sport',
    'surface',
    'toll',
    'tourism',
    'tower:type',
    'tracktype',
    'tunnel',
    'water',
    'waterway',
    'wetland',
    'width',
    'wood',
    'abandoned:aeroway',
    'abandoned:amenity',
    'abandoned:building',
    'abandoned:landuse',
    'abandoned:power',
    'area:highway'
}

-- The following keys will be deleted
local delete_keys = {
    'attribution',
    'comment',
    'created_by',
    'fixme',
    'note',
    'note:*',
    'odbl',
    'odbl:note',
    'source',
    'source:*',
    'source_ref',
    'way',
    'way_area',
    'z_order',
}

local point_columns = {
}

local non_point_columns = {
}

function gen_columns(text_columns, with_hstore, area, geometry_type)
    columns = {}

    local add_column = function (name, type)
        columns[#columns + 1] = { column = name, type = type }
    end

    for _, c in ipairs(text_columns) do
        add_column(c, 'text')
    end

    add_column('z_order', 'int')

    if area ~= nil then
        if area then
            add_column('way_area', 'area')
        else
            add_column('way_area', 'hstore')
        end
    end

    if hstore_column then
        add_column(hstore_column, 'hstore')
    end

    if with_hstore then
        add_column('tags', 'hstore')
    end

    add_column('way', geometry_type)
    columns[#columns].projection = srid

    return columns
end

local tables = {}

--for storing node tags later
local disputed = {}
local claimed = {}


tables.point = osm2pgsql.define_table{
    name = prefix .. '_point',
    ids = { type = 'node', id_column = 'osm_id' },
    columns = gen_columns(point_columns, hstore or hstore_all, nil, 'point')
}

tables.line = osm2pgsql.define_table{
    name = prefix .. '_line',
    ids = { type = 'way', id_column = 'osm_id' },
    columns = gen_columns(non_point_columns, hstore or hstore_all, false, 'linestring')
}

tables.polygon = osm2pgsql.define_table{
    name = prefix .. '_polygon',
    ids = { type = 'area', id_column = 'osm_id' },
    columns = gen_columns(non_point_columns, hstore or hstore_all, true, 'geometry')
}

tables.roads = osm2pgsql.define_table{
    name = prefix .. '_roads',
    ids = { type = 'way', id_column = 'osm_id' },
    columns = gen_columns(non_point_columns, hstore or hstore_all, false, 'linestring')
}

local z_order_lookup = {
    proposed = {1, false},
    construction = {2, false},
    steps = {10, false},
    cycleway = {10, false},
    bridleway = {10, false},
    footway = {10, false},
    path = {10, false},
    track = {11, false},
    service = {15, false},

    tertiary_link = {24, false},
    secondary_link = {25, true},
    primary_link = {27, true},
    trunk_link = {28, true},
    motorway_link = {29, true},

    raceway = {30, false},
    pedestrian = {31, false},
    living_street = {32, false},
    road = {33, false},
    unclassified = {33, false},
    residential = {33, false},
    tertiary = {34, false},
    secondary = {36, true},
    primary = {37, true},
    trunk = {38, true},
    motorway = {39, true}
}

function as_bool(value)
    return value == 'yes' or value == 'true' or value == '1'
end

function get_z_order(tags)
    local z_order = 100 * math.floor(tonumber(tags.layer or '0') or 0)
    local roads = false

    local highway = tags['highway']
    if highway then
        local r = z_order_lookup[highway] or {0, false}
        z_order = z_order + r[1]
        roads = r[2]
    end

    if tags.railway then
        z_order = z_order + 35
        roads = true
    end

    if tags.boundary and tags.boundary == 'administrative' then
        roads = true
    end

    if as_bool(tags.bridge) then
        z_order = z_order + 100
    end

    if as_bool(tags.tunnel) then
        z_order = z_order - 100
    end

    return z_order, roads
end

function make_check_in_list_func(list)
    local h = {}
    for _, k in ipairs(list) do
        h[k] = true
    end
    return function(tags)
        for k, _ in pairs(tags) do
            if h[k] then
                return true
            end
        end
        return false
    end
end

local is_polygon = make_check_in_list_func(polygon_keys)
local clean_tags = osm2pgsql.make_clean_tags_func(delete_keys)

function make_column_hash(columns)
    local h = {}

    for _, k in ipairs(columns) do
        h[k] = true
    end

    return h
end

function make_get_output(columns, hstore_all)
    local h = make_column_hash(columns)
    if hstore_all then
        return function(tags)
            local output = {}
            local hstore_entries = {}

            for k, _ in pairs(tags) do
                if h[k] then
                    output[k] = tags[k]
                end
                hstore_entries[k] = tags[k]
            end

            return output, hstore_entries
        end
    else
        return function(tags)
            local output = {}
            local hstore_entries = {}

            for k, _ in pairs(tags) do
                if h[k] then
                    output[k] = tags[k]
                else
                    hstore_entries[k] = tags[k]
                end
            end

            return output, hstore_entries
        end
    end
end

local has_generic_tag = make_check_in_list_func(generic_keys)

local get_point_output = make_get_output(point_columns, hstore_all)
local get_non_point_output = make_get_output(non_point_columns, hstore_all)

function get_hstore_column(tags)
    local len = #hstore_column
    local h = {}
    for k, v in pairs(tags) do
        if k:sub(1, len) == hstore_column then
            h[k:sub(len + 1)] = v
        end
    end

    if next(h) then
        return h
    end
    return nil
end

function osm2pgsql.process_node(object)
    if clean_tags(object.tags) then
        return
    end

    local output
    local output_hstore = {}
    if hstore or hstore_all then
        output, output_hstore = get_point_output(object.tags)
        if not next(output) and not next(output_hstore) then
            return
        end
        if hstore_match_only and not has_generic_tag(object.tags) then
            return
        end
    else
        output = object.tags
        if not has_generic_tag(object.tags) then
            return
        end
    end

-- Add POV tags to certain place nodes to change label rendering
-- Hide Arunachal Pradesh region label for China POV
    if object.tags.place and object.tags.wikidata == 'Q1162' then
        output_hstore['disputed_by'] = 'CN'
    end
-- Hide Gilgit-Baltistan region label for India POV
    if object.tags.place and object.tags.wikidata == 'Q200697' then
        output_hstore['disputed_by'] = 'IN'
    end
-- Hide Azad Kashmir region label for India POV
    if object.tags.place and object.tags.wikidata == 'Q200130' then
        output_hstore['disputed_by'] = 'IN'
    end
-- Hide Ladakh region label for Pakistan POV
    if object.tags.place and object.tags.wikidata == 'Q200667' then
        output_hstore['disputed_by'] = 'PK'
    end
-- Recast Gaza Strip label as country
    if object.tags.place and object.tags.wikidata == 'Q39760' then
        output_hstore['place'] = 'country'
        output_hstore['place:ID'] = 'region'
        output_hstore['place:PK'] = 'region'
        output_hstore['place:SA'] = 'region'
    end
-- Recast West Bank label as country
    if object.tags.place and object.tags.wikidata == 'Q36678' then
       output_hstore['place'] = 'country'
       output_hstore['place:ID'] = 'region'
       output_hstore['place:PK'] = 'region'
       output_hstore['place:SA'] = 'region'
    end
-- Recast Western Sahara label as country expect for FR;IN;PS;SA;MA;TR;ID;Pl;NL
    if object.tags.place and object.tags.wikidata == 'Q6250' then
        output_hstore['place'] = 'country'
        output_hstore['disputed_by'] = 'FR;ID;IN;MA;NL;Pl;PS;SA;TR'
    end
-- Redefine Israel country label for SA;PK;ID
    if object.tags.place and object.tags.wikidata == 'Q801' then
        output_hstore["name:id"] = 'Palestina'
        output_hstore["name:ur"] = 'فلسطین'
        output_hstore["name:ar"] = 'فلسطين'
    end
-- Recast Taiwan country label as region label for China POV
    if object.tags.place and object.tags.wikidata == 'Q865' then
        output_hstore['place:CN'] = 'region'
    end
-- Recast Taiwan region to county labels for China POV
    if object.tags.place and (object.tags.wikidata == 'Q115256' or object.tags.wikidata == 'Q133865' or
        object.tags.wikidata == 'Q140631' or object.tags.wikidata == 'Q153221' or object.tags.wikidata == 'Q166977' or
        object.tags.wikidata == 'Q181557' or object.tags.wikidata == 'Q1867' or object.tags.wikidata == 'Q194989' or
        object.tags.wikidata == 'Q198525' or object.tags.wikidata == 'Q237258' or object.tags.wikidata == 'Q244898' or
        object.tags.wikidata == 'Q245023' or object.tags.wikidata == 'Q249868' or object.tags.wikidata == 'Q249870' or
        object.tags.wikidata == 'Q249872' or object.tags.wikidata == 'Q249904' or object.tags.wikidata == 'Q249994' or
        object.tags.wikidata == 'Q249995' or object.tags.wikidata == 'Q249996' or object.tags.wikidata == 'Q63706' or
        object.tags.wikidata == 'Q74054' or object.tags.wikidata == 'Q82357') then
        output_hstore['place:CN'] = 'county'
    end
-- Turn off Kosovo country label for CN;RU;IN;GR
    if object.tags.place and object.tags.wikidata == 'Q1246' then
        output_hstore['disputed_by'] = 'CN;GR;IN;RU'
        output_hstore['recognized_by'] = 'AR;BD;BR;DE;EG;ES;FR;GB;ID;IL;IT;JP;KO;MA;NL;NP;PK;PL;PS;PT;SA;SE;TR;TW;UA;US;VN'
    end
-- Hide Kosovo region labels for several POVs including China and Russia
    if object.tags.place and (object.tags.wikidata == 'Q1008042' or object.tags.wikidata == 'Q1021775' or
        object.tags.wikidata == 'Q112657' or object.tags.wikidata == 'Q124725' or object.tags.wikidata == 'Q15710469' or
        object.tags.wikidata == 'Q227569' or object.tags.wikidata == 'Q248378' or object.tags.wikidata == 'Q25270' or
        object.tags.wikidata == 'Q392505' or object.tags.wikidata == 'Q42328687' or object.tags.wikidata == 'Q474651' or
        object.tags.wikidata == 'Q4864476' or object.tags.wikidata == 'Q59074' or object.tags.wikidata == 'Q59086' or
        object.tags.wikidata == 'Q59089' or object.tags.wikidata == 'Q608274' or object.tags.wikidata == 'Q62172' or
        object.tags.wikidata == 'Q733155' or object.tags.wikidata == 'Q738901' or object.tags.wikidata == 'Q739808' or
        object.tags.wikidata == 'Q786124' or object.tags.wikidata == 'Q911241' or object.tags.wikidata == 'Q939112' or
        object.tags.wikidata == 'Q963121' or object.tags.wikidata == 'Q991291' or object.tags.wikidata == 'Q991291' or
        object.tags.wikidata == 'Q991313' or object.tags.wikidata == 'Q991332' or object.tags.wikidata == 'Q994245' or
        object.tags.wikidata == 'Q994730') then
        output_hstore['disputed_by'] = 'CN;RU;IN;GR'
    end
-- Recast Northern Cyprus as country label and turn off for several POVs including China and Russia
    if object.tags.place and object.tags.wikidata == 'Q23681' then
        output_hstore['place'] = 'country'
        output_hstore['disputed_by'] = 'CN;RU;IN;GR;CY'
    end
-- Turn off Abkhazia label for most countries
    if object.tags.place and object.tags.wikidata == 'Q23334' then
        output_hstore['place:AR'] = 'region'
        output_hstore['place:BD'] = 'region'
        output_hstore['place:BR'] = 'region'
        output_hstore['place:CN'] = 'region'
        output_hstore['place:DE'] = 'region'
        output_hstore['place:EG'] = 'region'
        output_hstore['place:GB'] = 'region'
        output_hstore['place:GR'] = 'region'
        output_hstore['place:ID'] = 'region'
        output_hstore['place:IL'] = 'region'
        output_hstore['place:IN'] = 'region'
        output_hstore['place:IT'] = 'region'
        output_hstore['place:JP'] = 'region'
        output_hstore['place:KO'] = 'region'
        output_hstore['place:MA'] = 'region'
        output_hstore['place:NL'] = 'region'
        output_hstore['place:NP'] = 'region'
        output_hstore['place:PK'] = 'region'
        output_hstore['place:PL'] = 'region'
        output_hstore['place:PS'] = 'region'
        output_hstore['place:PT'] = 'region'
        output_hstore['place:SA'] = 'region'
        output_hstore['place:SE'] = 'region'
        output_hstore['place:TR'] = 'region'
        output_hstore['place:TW'] = 'region'
        output_hstore['place:UA'] = 'region'
        output_hstore['place:VN'] = 'region'
    end
-- Turn off South Ossetia label for most countries
    if object.tags.place and object.tags.wikidata == 'Q23427' then
        output_hstore['place:AR'] = 'region'
        output_hstore['place:BD'] = 'region'
        output_hstore['place:BR'] = 'region'
        output_hstore['place:CN'] = 'region'
        output_hstore['place:DE'] = 'region'
        output_hstore['place:EG'] = 'region'
        output_hstore['place:GB'] = 'region'
        output_hstore['place:GR'] = 'region'
        output_hstore['place:ID'] = 'region'
        output_hstore['place:IL'] = 'region'
        output_hstore['place:IN'] = 'region'
        output_hstore['place:IT'] = 'region'
        output_hstore['place:JP'] = 'region'
        output_hstore['place:KO'] = 'region'
        output_hstore['place:MA'] = 'region'
        output_hstore['place:NL'] = 'region'
        output_hstore['place:NP'] = 'region'
        output_hstore['place:PK'] = 'region'
        output_hstore['place:PL'] = 'region'
        output_hstore['place:PS'] = 'region'
        output_hstore['place:PT'] = 'region'
        output_hstore['place:SA'] = 'region'
        output_hstore['place:SE'] = 'region'
        output_hstore['place:TR'] = 'region'
        output_hstore['place:TW'] = 'region'
        output_hstore['place:UA'] = 'region'
        output_hstore['place:VN'] = 'region'
    end
-- Turn off Nagorno-Karabakh label for most countries
    if object.tags.place and object.tags.wikidata == 'Q2397204' then
        output_hstore['place:AR'] = 'region'
        output_hstore['place:BD'] = 'region'
        output_hstore['place:BR'] = 'region'
        output_hstore['place:CN'] = 'region'
        output_hstore['place:DE'] = 'region'
        output_hstore['place:EG'] = 'region'
        output_hstore['place:ES'] = 'region'
        output_hstore['place:FR'] = 'region'
        output_hstore['place:GB'] = 'region'
        output_hstore['place:GR'] = 'region'
        output_hstore['place:ID'] = 'region'
        output_hstore['place:IL'] = 'region'
        output_hstore['place:IN'] = 'region'
        output_hstore['place:IT'] = 'region'
        output_hstore['place:JP'] = 'region'
        output_hstore['place:KO'] = 'region'
        output_hstore['place:MA'] = 'region'
        output_hstore['place:NL'] = 'region'
        output_hstore['place:NP'] = 'region'
        output_hstore['place:PK'] = 'region'
        output_hstore['place:PL'] = 'region'
        output_hstore['place:PS'] = 'region'
        output_hstore['place:PT'] = 'region'
        output_hstore['place:RU'] = 'region'
        output_hstore['place:SA'] = 'region'
        output_hstore['place:SE'] = 'region'
        output_hstore['place:TR'] = 'region'
        output_hstore['place:TW'] = 'region'
        output_hstore['place:US'] = 'region'
        output_hstore['place:VN'] = 'region'
    end
-- Turn off Somaliland label for most countries
    if object.tags.place and object.tags.wikidata == 'Q34754' then
        output_hstore['place:AR'] = 'region'
        output_hstore['place:BD'] = 'region'
        output_hstore['place:BR'] = 'region'
        output_hstore['place:CN'] = 'region'
        output_hstore['place:EG'] = 'region'
        output_hstore['place:GR'] = 'region'
        output_hstore['place:ID'] = 'region'
        output_hstore['place:IL'] = 'region'
        output_hstore['place:IN'] = 'region'
        output_hstore['place:MA'] = 'region'
        output_hstore['place:NP'] = 'region'
        output_hstore['place:PK'] = 'region'
        output_hstore['place:PL'] = 'region'
        output_hstore['place:PS'] = 'region'
        output_hstore['place:PT'] = 'region'
        output_hstore['place:RU'] = 'region'
        output_hstore['place:SA'] = 'region'
        output_hstore['place:SO'] = 'region'
        output_hstore['place:TR'] = 'region'
        output_hstore['place:TW'] = 'region'
        output_hstore['place:UA'] = 'region'
        output_hstore['place:VN'] = 'region'
    end

    output.tags = output_hstore

    if hstore_column then
        output[hstore_column] = get_hstore_column(object.tags)
    end

    tables.point:add_row(output)
end

function osm2pgsql.process_way(object)
    if clean_tags(object.tags) then
        return
    end

    local add_area = false
    if object.tags.natural == 'coastline' then
        add_area = true
        if not keep_coastlines then
            object.tags.natural = nil
        end
    end

    local output
    local output_hstore = {}
    if hstore or hstore_all then
        output, output_hstore = get_non_point_output(object.tags)
        if not next(output) and not next(output_hstore) then
            return
        end
        if hstore_match_only and not has_generic_tag(object.tags) then
            return
        end
        if add_area and hstore_all then
            output_hstore.area = 'yes'
        end
    else
        output = object.tags
        if not has_generic_tag(object.tags) then
            return
        end
    end

    local polygon
    local area_tag = object.tags.area
    if area_tag == 'yes' or area_tag == '1' or area_tag == 'true' then
        polygon = true
    elseif area_tag == 'no' or area_tag == '0' or area_tag == 'false' then
        polygon = false
    else
        polygon = is_polygon(object.tags)
    end

    if add_area then
        output.area = 'yes'
        polygon = true
    end

    local z_order, roads = get_z_order(object.tags)
    output.z_order = z_order

-- Stripped disputed tags off of ways
    if object.tags.claimed_by or object.tags.disputed_by or object.tags.recognized_by or object.tags.dispute then
        output_hstore.claimed_by = nil
        output_hstore.disputed_by = nil
        output_hstore.recognized_by = nil
        output_hstore.dispute = nil
        output_hstore.disputed = nil
    end

-- Redefine extra disputed admin ways as administrative to avoid them
    if object.tags.boundary == 'disputed' then
        output_hstore.boundary = 'administrative'
    end

-- Adds suppress any ways involved with claims. The claim relation will render instead for everyone.
    for k, v in pairs(claimed) do
        if k == object.id then
            output_hstore.dispute = 'yes'
            output_hstore.unrecognized_dispute = 'yes'
            if v.disputed_by then
                output_hstore.disputed_by = 'AR;BD;BR;CN;DE;EG;ES;FR;GB;GR;ID;IL;IN;IT;JP;KO;MA;NL;NP;PK;PL;PS;PT;RU;SA;SE;TR;TW;UA;US;VN'
            end
        end
    end

-- Adds dispute tags to ways in disputed relations
    for k, v in pairs(disputed) do
        if k == object.id then
            output_hstore.dispute = 'yes'
            if v.disputed_by then
                output_hstore.disputed_by = v.disputed_by
            end
            if v.claimed_by then
                output_hstore.claimed_by = v.claimed_by
            end
            if v.recognized_by then
                output_hstore.recognized_by = v.recognized_by
            end
            if v['unrecognized_dispute'] then
                output_hstore.unrecognized_dispute = 'yes'
            end
        end
    end

    output.tags = output_hstore

    if hstore_column then
        output[hstore_column] = get_hstore_column(object.tags)
    end

    if polygon and object.is_closed then
        output.way = { create = 'area' }
        tables.polygon:add_row(output)
    else
        output.way = { create = 'line', split_at = max_length }
        tables.line:add_row(output)
        if roads then
            tables.roads:add_row(output)
        end
    end
end

function osm2pgsql.select_relation_members(relation)
    if relation.tags.type == 'boundary' or relation.tags.type == 'linestring' then
        return { ways = osm2pgsql.way_member_ids(relation) }
    end
end

function osm2pgsql.process_relation(object)
    if clean_tags(object.tags) then
        return
    end

    local type = object.tags.type
    if (type ~= 'route') and (type ~= 'multipolygon') and (type ~= 'boundary') and (type ~= 'linestring') then
        return
    end
    object.tags.type = nil

    local output
    local output_hstore = {}
    if hstore or hstore_all then
        output, output_hstore = get_non_point_output(object.tags)
        if not next(output) and not next(output_hstore) then
            return
        end
        if hstore_match_only and not has_generic_tag(object.tags) then
            return
        end
    else
        output = object.tags
        if not has_generic_tag(object.tags) then
            return
        end
    end

    if not next(output) and not next(output_hstore) then
        return
    end

-- Mark some disputes as unrecognized to hide them by default
    if (type == 'linestring' or type == 'boundary') and (object.tags['ne:brk_a3'] == 'B20' or object.tags['ne:brk_a3'] == 'B35'
    or object.tags['ne:brk_a3'] == 'B37' or object.tags['ne:brk_a3'] == 'B38' or object.tags['ne:brk_a3'] == 'B43' or
    object.tags['ne:brk_a3'] == 'B75' or object.tags['ne:brk_a3'] == 'B90' or object.tags['ne:brk_a3'] == 'C02' or
    object.tags['ne:brk_a3'] == 'C03') then
        output_hstore.unrecognized_dispute = 'yes'
    end

-- Adds tags from boundary=claim relation to its ways
    if (type == 'linestring' or type == 'boundary') and object.tags.boundary == 'claim' and object.tags.admin_level == '4' then
        for _, member in ipairs(object.members) do
            if member.type == 'w' then
                if not claimed[member.ref] then
                    claimed[member.ref] = {}
                end
                claimed[member.ref] = object.tags
            end
        end
    end

-- Adds tags from boundary=disputed relation to its ways
    if (type == 'linestring' or type == 'boundary') and (object.tags.boundary == 'disputed') then
        for _, member in ipairs(object.members) do
            if member.type == 'w' then
                if not disputed[member.ref] then
                    disputed[member.ref] = {}
                end
                disputed[member.ref] = object.tags
            end
        end
    end

-- Adds tags to redefine Taiwan admin levels.
    if type == 'boundary' and (object.tags.admin_level == '4' or object.tags.admin_level == '6') and object.tags['ISO3166-2'] then
        if osm2pgsql.has_prefix(object.tags['ISO3166-2'], 'TW-') then
            output_hstore.admin_level = '4'
            output_hstore['admin_level:CN'] = '6'
        end
    end

-- Adds tags to redefine Israel admin 4 boundaries for Palestine.
    if type == 'boundary' and (object.tags.admin_level == '4') and object.tags['ISO3166-2'] then
        if osm2pgsql.has_prefix(object.tags['ISO3166-2'], 'IL-') then
            output_hstore['admin_level:BD'] = '8'
            output_hstore['admin_level:ID'] = '8'
            output_hstore['admin_level:PK'] = '8'
            output_hstore['admin_level:PS'] = '8'
            output_hstore['admin_level:SA'] = '8'
        end
    end

-- Add tags to redefine Hong Kong and Macau as admin 2 except for China which is Admin 4
    if type == 'boundary' and (object.tags['ISO3166-1'] == 'MO' or object.tags['ISO3166-1'] == 'HK') then
        output_hstore['admin_level'] = '2'
        output_hstore['admin_level:CN'] = '4'
    end

-- Convert admin_level 5 boundaries in Northern Cyprus to 4
    if type == 'boundary' and object.tags.is_in == 'Northern Cyprus' and object.tags.admin_level == '5' then
        output_hstore['admin_level'] = '4'
    end

-- Turn off West Bank and Judea and Samaria relations
    if type == 'boundary' and object.tags.wikidata == 'Q36678' then
        output_hstore = {}
    end
    if type == 'boundary' and object.tags.wikidata == 'Q513200' then
        output_hstore = {}
    end

-- Fix Kosovo dispute viewpoints
    if type == 'linestring' and object.tags.ne_id == '1746706755' then
        output_hstore['recognized_by'] = 'AR;BD;BR;DE;EG;ES;FR;GB;ID;IL;IT;JP;KO;MA;NL;NP;PK;PL;PS;PT;SA;SE;TR;TW;UA;US;VN'
    end

    if enable_legacy_route_processing and (hstore or hstore_all) and type == 'route' then
        if not object.tags.route_name then
            output_hstore.route_name = object.tags.name
        end

        local state = object.tags.state
        if state ~= 'alternate' and state ~= 'connection' then
            state = 'yes'
        end

        local network = object.tags.network
        if network == 'lcn' then
            output_hstore.lcn = output_hstore.lcn or state
            output_hstore.lcn_ref = output_hstore.lcn_ref or object.tags.ref
        elseif network == 'rcn' then
            output_hstore.rcn = output_hstore.rcn or state
            output_hstore.rcn_ref = output_hstore.rcn_ref or object.tags.ref
        elseif network == 'ncn' then
            output_hstore.ncn = output_hstore.ncn or state
            output_hstore.ncn_ref = output_hstore.ncn_ref or object.tags.ref
        elseif network == 'lwn' then
            output_hstore.lwn = output_hstore.lwn or state
            output_hstore.lwn_ref = output_hstore.lwn_ref or object.tags.ref
        elseif network == 'rwn' then
            output_hstore.rwn = output_hstore.rwn or state
            output_hstore.rwn_ref = output_hstore.rwn_ref or object.tags.ref
        elseif network == 'nwn' then
            output_hstore.nwn = output_hstore.nwn or state
            output_hstore.nwn_ref = output_hstore.nwn_ref or object.tags.ref
        end

        local pc = object.tags.preferred_color
        if pc == '0' or pc == '1' or pc == '2' or pc == '3' or pc == '4' then
            output_hstore.route_pref_color = pc
        else
            output_hstore.route_pref_color = '0'
        end
    end

    local make_boundary = false
    local make_polygon = false
    if type == 'boundary' then
        make_boundary = true
    elseif type == 'multipolygon' and object.tags.boundary then
        make_boundary = true
    elseif type == 'multipolygon' then
        make_polygon = true
    end

    local z_order, roads = get_z_order(object.tags)
    output.z_order = z_order

    output.tags = output_hstore

    if hstore_column then
        output[hstore_column] = get_hstore_column(object.tags)
    end

    if not make_polygon then
        output.way = { create = 'line', split_at = max_length }
        tables.line:add_row(output)
        if roads then
            tables.roads:add_row(output)
        end
    end

    if make_boundary or make_polygon then
        output.way = { create = 'area' }
        if not multi_geometry then
            output.way.split_at = 'multi'
        end
        tables.polygon:add_row(output)
    end
end
