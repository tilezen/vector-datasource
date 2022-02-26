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
local n2r = {}
local twadmin = {}
local disputed = {}
local province_dispute = {}
local cyprus_ways = {}


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

    output.tags = output_hstore

    if hstore_column then
        output[hstore_column] = get_hstore_column(object.tags)
    end

--	Pulls out place tag for adding to relation later
    if object.tags.place then
        if not n2r[object.id] then
            n2r[object.id] = {}
        end
        n2r[object.id] = object.tags.place
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
    end

    if object.tags.boundary == 'disputed' then
        output_hstore.boundary = 'administrative'
    end

-- Adds tags to redefine Taiwan admin levels. Applies to both relation and ways
    for k, v in pairs(twadmin) do
        if k == object.id then
            output_hstore.admin_level = '4'
            output_hstore['admin_level:AR'] = '4'
            output_hstore['admin_level:BD'] = '4'
            output_hstore['admin_level:BR'] = '4'
            output_hstore['admin_level:CN'] = '6'
            output_hstore['admin_level:DE'] = '4'
            output_hstore['admin_level:EG'] = '4'
            output_hstore['admin_level:ES'] = '4'
            output_hstore['admin_level:FR'] = '4'
            output_hstore['admin_level:GB'] = '4'
            output_hstore['admin_level:GR'] = '4'
            output_hstore['admin_level:ID'] = '4'
            output_hstore['admin_level:IL'] = '4'
            output_hstore['admin_level:IN'] = '4'
            output_hstore['admin_level:IT'] = '4'
            output_hstore['admin_level:JP'] = '4'
            output_hstore['admin_level:KO'] = '4'
            output_hstore['admin_level:MA'] = '4'
            output_hstore['admin_level:NL'] = '4'
            output_hstore['admin_level:NP'] = '4'
            output_hstore['admin_level:PK'] = '4'
            output_hstore['admin_level:PL'] = '4'
            output_hstore['admin_level:PS'] = '4'
            output_hstore['admin_level:PT'] = '4'
            output_hstore['admin_level:SA'] = '4'
            output_hstore['admin_level:SE'] = '4'
            output_hstore['admin_level:TR'] = '4'
            output_hstore['admin_level:TW'] = '4'
            output_hstore['admin_level:UA'] = '4'
            output_hstore['admin_level:US'] = '4'
            output_hstore['admin_level:VN'] = '4'
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
        end
    end

-- adds tags from province level dispute relations
    for k, v in pairs(province_dispute) do
        if k == object.id then
            for a, i in pairs(v) do
                if not output_hstore[a] then
                    output_hstore[a] = i
                end
            end
        end
    end

-- Convert admin_level 5 boundaries in Northern Cyprus to 4
    for _, v in pairs(cyprus_ways) do
        if v == object.id then
            output_hstore.admin_level = '4'
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

--	Filters on boundaries with a label role node
--	Compares node to n2r ids and adds place tag to relation if a match occurs
    if type == 'boundary' and object.tags.admin_level == '3' and object.tags.wikidata ~= 'Q205047' then
        for _, member in ipairs(object.members) do
            if member.role == 'label' then
                for k, v in pairs(n2r) do
                    if k == member.ref then
                        output_hstore.place = v
                    end
                end
            end
        end
    end

-- Adds tags to redefine Taiwan admin levels. Applies to both relation and ways.
    if type == 'boundary' and (object.tags.admin_level == '4' or object.tags.admin_level == '6') and object.tags['ISO3166-2'] then
        if osm2pgsql.has_prefix(object.tags['ISO3166-2'], 'TW-') then
            for _, member in ipairs(object.members) do
                if member.type == 'w' then
                    if not twadmin[member.ref] then
                        twadmin[member.ref] = {}
                    end
                    twadmin[member.ref] = object.id
                end
            end
            output_hstore.admin_level = '4'
            output_hstore['admin_level:AR'] = '4'
            output_hstore['admin_level:BD'] = '4'
            output_hstore['admin_level:BR'] = '4'
            output_hstore['admin_level:CN'] = '6'
            output_hstore['admin_level:DE'] = '4'
            output_hstore['admin_level:EG'] = '4'
            output_hstore['admin_level:ES'] = '4'
            output_hstore['admin_level:FR'] = '4'
            output_hstore['admin_level:GB'] = '4'
            output_hstore['admin_level:GR'] = '4'
            output_hstore['admin_level:ID'] = '4'
            output_hstore['admin_level:IL'] = '4'
            output_hstore['admin_level:IN'] = '4'
            output_hstore['admin_level:IT'] = '4'
            output_hstore['admin_level:JP'] = '4'
            output_hstore['admin_level:KO'] = '4'
            output_hstore['admin_level:MA'] = '4'
            output_hstore['admin_level:NL'] = '4'
            output_hstore['admin_level:NP'] = '4'
            output_hstore['admin_level:PK'] = '4'
            output_hstore['admin_level:PL'] = '4'
            output_hstore['admin_level:PS'] = '4'
            output_hstore['admin_level:PT'] = '4'
            output_hstore['admin_level:SA'] = '4'
            output_hstore['admin_level:SE'] = '4'
            output_hstore['admin_level:TR'] = '4'
            output_hstore['admin_level:TW'] = '4'
            output_hstore['admin_level:UA'] = '4'
            output_hstore['admin_level:US'] = '4'
            output_hstore['admin_level:VN'] = '4'
        end
    end

-- Adds tags to turn off Israel admin 4 boundaries for Palestine.
    if type == 'boundary' and (object.tags.admin_level == '4') and object.tags['ISO3166-2'] then
        if osm2pgsql.has_prefix(object.tags['ISO3166-2'], 'IL-') then
            output_hstore['admin_level:PS'] = '6'
        end
    end

-- Adds tags to redefine other relation admin levels, based on relation. Applies to both relation and ways.
    if type == 'linestring' and object.tags.boundary == 'claim' and object.tags.claimed_by == nil then
        for _, member in ipairs(object.members) do
            if member.type == 'w' then
                if not province_dispute[member.ref] then
                    province_dispute[member.ref] = {}
                end
                province_dispute[member.ref] = object.tags
            end
        end
    end

-- Adds dispute=yes to any ways part of a boundary=disputed relation
    if (type == 'linestring' or type == 'boundary') and object.tags.boundary == 'disputed' then
        for _, member in ipairs(object.members) do
            if member.type == 'w' then
                if not disputed[member.ref] then
                    disputed[member.ref] = {}
                end
                disputed[member.ref] = object.tags
            end
        end
        output_hstore.dispute = 'yes'
    end

    if type == 'boundary' and (object.tags['ISO3166-1'] == 'MO' or object.tags['ISO3166-1'] == 'HK') then
        output_hstore['admin_level'] = '2'
        output_hstore['admin_level:AR'] = '2'
        output_hstore['admin_level:BD'] = '2'
        output_hstore['admin_level:BR'] = '2'
        output_hstore['admin_level:CN'] = '4'
        output_hstore['admin_level:DE'] = '2'
        output_hstore['admin_level:EG'] = '2'
        output_hstore['admin_level:ES'] = '2'
        output_hstore['admin_level:FR'] = '2'
        output_hstore['admin_level:GB'] = '2'
        output_hstore['admin_level:GR'] = '2'
        output_hstore['admin_level:ID'] = '2'
        output_hstore['admin_level:IL'] = '2'
        output_hstore['admin_level:IN'] = '2'
        output_hstore['admin_level:IT'] = '2'
        output_hstore['admin_level:JP'] = '2'
        output_hstore['admin_level:KO'] = '2'
        output_hstore['admin_level:MA'] = '2'
        output_hstore['admin_level:NL'] = '2'
        output_hstore['admin_level:NP'] = '2'
        output_hstore['admin_level:PK'] = '2'
        output_hstore['admin_level:PL'] = '2'
        output_hstore['admin_level:PS'] = '2'
        output_hstore['admin_level:PT'] = '2'
        output_hstore['admin_level:SA'] = '2'
        output_hstore['admin_level:SE'] = '2'
        output_hstore['admin_level:TR'] = '2'
        output_hstore['admin_level:TW'] = '2'
        output_hstore['admin_level:UA'] = '2'
        output_hstore['admin_level:US'] = '2'
        output_hstore['admin_level:VN'] = '2'
    end

-- Convert admin_level 5 boundaries in Northern Cyprus to 4
    if type == 'boundary' and object.tags.is_in == 'Northern Cyprus' and object.tags.admin_level == '5' then
        output_hstore.admin_level = '4'
        cyprus_ways = osm2pgsql.way_member_ids(object)
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
