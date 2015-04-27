-- used to check whether an index exists before adding
CREATE OR REPLACE FUNCTION mz_does_index_exist(index_name text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM pg_class AS c
        INNER JOIN pg_namespace AS n ON n.oid = c.relnamespace
        WHERE c.relname = index_name
    );
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_does_trigger_exist(trigger_name text, table_name text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS(
        SELECT 1 FROM pg_class AS c
        INNER JOIN pg_namespace AS n ON n.oid = c.relnamespace
        INNER JOIN pg_trigger AS t ON t.tgrelid = c.oid
        WHERE c.relname = table_name
          AND t.tgname = trigger_name
    );
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_create_index_if_not_exists(index_name text, table_name text, column_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_index_exist(index_name) THEN
        EXECUTE 'CREATE INDEX ' ||
            quote_ident(index_name) || ' ON ' || quote_ident(table_name) ||
            '(' || quote_ident(column_name) || ')';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_create_partial_index_if_not_exists(index_name text, table_name text, column_name text, where_clause text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_index_exist(index_name) THEN
        EXECUTE 'CREATE INDEX ' ||
            quote_ident(index_name) || ' ON ' || quote_ident(table_name) ||
            '(' || quote_ident(column_name) || ') WHERE ' || where_clause;
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_create_trigger_if_not_exists(
    trigger_name text, table_name text, function_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_trigger_exist(trigger_name, table_name) THEN
        EXECUTE 'CREATE TRIGGER ' || quote_ident(trigger_name) ||
          ' BEFORE INSERT OR UPDATE ON ' || quote_ident(table_name) ||
          ' FOR EACH ROW EXECUTE PROCEDURE ' || quote_ident(function_name) || '()';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_does_column_exist(input_table_name text, input_column_name text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name=input_table_name AND column_name=input_column_name
    );
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_add_simplified_geometry_column(
    table_name text, column_name text, existing_geom_column_name text, geom_type text, tolerance float, where_clause text default NULL)
RETURNS VOID AS $$
DECLARE v_where_clause TEXT DEFAULT '';
DECLARE v_index_where TEXT DEFAULT '';
BEGIN
    IF NOT mz_does_column_exist(table_name, column_name) THEN
        PERFORM AddGeometryColumn(table_name, column_name, 900913, geom_type, 2);
        IF where_clause IS NOT NULL THEN
            v_where_clause := ' AND ' || where_clause;
            v_index_where := ' WHERE ' || where_clause;
        END IF;
        EXECUTE 'UPDATE ' || quote_ident(table_name) ||
            ' SET ' || quote_ident(column_name) ||
            '=ST_SimplifyPreserveTopology(' || quote_ident(existing_geom_column_name) ||
            ', ' || tolerance || ')' ||
            ' WHERE ' || quote_ident(existing_geom_column_name) || ' IS NOT NULL' ||
            v_where_clause;
        EXECUTE 'CREATE INDEX ' || quote_ident(table_name || '_' || column_name) ||
            ' ON ' || quote_ident(table_name) || ' USING gist(' || quote_ident(column_name) || ')' ||
            v_index_where;
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_safe_convert_to_float(v_input text)
RETURNS FLOAT AS $$
DECLARE v_float_value FLOAT DEFAULT NULL;
BEGIN
    BEGIN
        v_float_value := TO_NUMBER(
            REPLACE(REPLACE(v_input, ';', '.'), ',', '.'),
            '999999D99S') AS FLOAT;
    EXCEPTION WHEN OTHERS THEN
        RETURN NULL;
    END;
    RETURN v_float_value;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_normalize_id(id bigint, geom Geometry)
RETURNS TEXT AS $$
BEGIN
    IF id < 0 THEN
        RETURN Substr(MD5(ST_AsBinary(geom)), 1, 10);
    ELSE
        RETURN id::text;
    END IF;
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION mz_add_normalized_id(
    table_name text, column_name text, geom_name text, prev_id_column_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_column_exist(table_name, column_name) THEN
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' ADD COLUMN ' || quote_ident(column_name) ||
                ' TEXT';
        EXECUTE 'UPDATE ' || quote_ident(table_name) ||
                ' SET ' || quote_ident(column_name) ||
                ' = mz_normalize_id(' || quote_ident(prev_id_column_name) ||
                ', ' || quote_ident(geom_name) || ')' ||
                ' WHERE ' || quote_ident(prev_id_column_name) || ' IS NOT NULL';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_add_area_column(table_name text, column_name text, geom_name text)
RETURNS VOID AS $$
BEGIN
    IF NOT mz_does_column_exist(table_name, column_name) THEN
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' ADD COLUMN ' || quote_ident(column_name) ||
                ' REAL';
        EXECUTE 'UPDATE ' || quote_ident(table_name) || ' SET ' || quote_ident(column_name) ||
                ' = ST_Area(' || quote_ident(geom_name) || ') ' ||
                'WHERE ' || quote_ident(geom_name) || ' IS NOT NULL';
    END IF;
END;
$$ LANGUAGE plpgsql VOLATILE;

-- functions to encapsulate logic for calculating new columns

CREATE OR REPLACE FUNCTION mz_calculate_is_landuse(
    landuse_val text, leisure_val text, natural_val text, highway_val text, amenity_val text, aeroway_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN
        landuse_val IN ('park', 'forest', 'residential', 'retail', 'commercial',
                        'industrial', 'railway', 'cemetery', 'grass', 'farmyard',
                        'farm', 'farmland', 'wood', 'meadow', 'village_green',
                        'recreation_ground', 'allotments', 'quarry')
     OR leisure_val IN ('park', 'garden', 'playground', 'golf_course', 'sports_centre',
                        'pitch', 'stadium', 'common', 'nature_reserve')
     OR natural_val IN ('wood', 'land', 'scrub', 'wetland', 'glacier')
     OR highway_val IN ('pedestrian', 'footway')
     OR amenity_val IN ('university', 'school', 'college', 'library', 'fuel',
                        'parking', 'cinema', 'theatre', 'place_of_worship', 'hospital')
     OR aeroway_val IN ('runway', 'taxiway', 'apron');
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_poi_level(
    aerialway_val text,
    aeroway_val text,
    amenity_val text,
    barrier_val text,
    highway_val text,
    historic_val text,
    leisure_val text,
    lock_val text,
    man_made_val text,
    natural_val text,
    power_val text,
    railway_val text,
    shop_val text,
    tourism_val text,
    waterway_val text
)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN aeroway_val IN ('aerodrome', 'airport') THEN 9
             WHEN natural_val IN ('peak', 'volcano') THEN 11
             WHEN railway_val IN ('station') THEN 12
             WHEN (aerialway_val IN ('station')
                   OR railway_val IN ('halt', 'tram_stop')
                   OR tourism_val IN ('alpine_hut')) THEN 13
             WHEN (natural_val IN ('spring')
                   OR railway_val IN ('level_crossing')) THEN 14
             WHEN (amenity_val IN ('hospital', 'parking')
                   OR barrier_val IN ('gate')
                   OR highway_val IN ('gate', 'mini_roundabout')
                   OR lock_val IN ('yes')
                   OR man_made_val IN ('lighthouse', 'power_wind')
                   OR natural_val IN ('cave_entrance')
                   OR power_val IN ('generator')
                   OR waterway_val IN ('lock')) THEN 15
             WHEN (aeroway_val IN ('helipad')
                   OR amenity_val IN ('biergarten', 'bus_station', 'bus_stop', 'car_sharing',
                                    'picnic_site', 'place_of_worship',
                                    'prison', 'pub', 'recycling', 'shelter')
                   OR barrier_val IN ('block', 'bollard', 'lift_gate')
                   OR highway_val IN ('bus_stop', 'ford')
                   OR historic_val IN ('archaeological_site')
                   OR man_made_val IN ('windmill')
                   OR natural_val IN ('tree')
                   OR shop_val IN ('department_store', 'supermarket')
                   OR tourism_val IN ('camp_site', 'caravan_site', 'information', 'viewpoint')) THEN 16
             WHEN (aeroway_val IN ('gate')
                   OR amenity_val IN (
                 'atm', 'bank', 'bar', 'bicycle_rental',
                 'cafe', 'cinema', 'courthouse', 'drinking_water', 'embassy', 'emergency_phone',
                 'fast_food', 'fire_station', 'fuel', 'library', 'pharmacy',
                 'police', 'post_box', 'post_office', 'restaurant', 'telephone', 'theatre',
                 'toilets', 'veterinary')
                   OR highway_val IN ('traffic_signals')
                   OR historic_val IN ('memorial')
                   OR leisure_val IN ('playground', 'slipway')
                   OR man_made_val IN ('mast', 'water_tower')
                   OR shop_val IN ('bakery', 'bicycle', 'books', 'butcher', 'car', 'car_repair',
                                 'clothes', 'computer', 'convenience',
                                 'doityourself', 'dry_cleaning', 'fashion', 'florist', 'gift',
                                 'greengrocer', 'hairdresser', 'jewelry', 'mobile_phone',
                                 'optician', 'pet')
                   OR tourism_val IN ('bed_and_breakfast', 'chalet', 'guest_house',
                                    'hostel', 'hotel', 'motel', 'museum')) THEN 17
             WHEN (amenity_val IN ('bench', 'waste_basket')
                   OR railway_val IN ('subway_entrance')) THEN 18
             ELSE NULL END
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_road_level(highway_val text, railway_val text, aeroway_val text)
RETURNS SMALLINT AS $$
BEGIN
    RETURN (
        CASE WHEN highway_val IN ('motorway') THEN 7
             WHEN highway_val IN ('trunk', 'primary', 'secondary') THEN 10
             WHEN (highway_val IN ('tertiary')
                OR aeroway_val IN ('runway', 'taxiway')) THEN 11
             WHEN highway_val IN ('motorway_link', 'trunk_link', 'residential', 'unclassified', 'road') THEN 12
             WHEN highway_val IN ('primary_link', 'secondary_link') THEN 13
             WHEN (highway_val IN ('tertiary_link', 'minor')
                OR railway_val IN ('rail', 'subway')) THEN 14
             WHEN (highway_val IN ('service', 'footpath', 'track', 'footway', 'steps', 'pedestrian', 'path', 'cycleway', 'living_street')
                OR railway_val IN ('tram', 'light_rail', 'narrow_gauge', 'monorail')) THEN 15
             ELSE NULL END
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_road_sort_key(
    layer_val text, bridge_val text, tunnel_val text, highway_val text, railway_val text, aeroway_val text)
RETURNS FLOAT AS $$
DECLARE v_layer_as_float FLOAT DEFAULT NULL;
BEGIN
    v_layer_as_float := mz_safe_convert_to_float(layer_val);
    RETURN (
        (CASE WHEN v_layer_as_float IS NOT NULL THEN 1000 * v_layer_as_float
            ELSE 0
            END)

        +

        --
        -- Bridges and tunnels have an implicit physical layering.
        --
        (CASE WHEN bridge_val IN ('yes', 'true') THEN 100
            WHEN tunnel_val IN ('yes', 'true') THEN -100
            ELSE 0
            END)

        +

        --
        -- Large roads are drawn on top of smaller roads.
        --
        (CASE WHEN highway_val IN ('motorway') THEN 0
            WHEN railway_val IN ('rail', 'tram', 'light_rail', 'narrow_guage', 'monorail') THEN -.5
            WHEN highway_val IN ('trunk') THEN -1
            WHEN highway_val IN ('primary') THEN -2
            WHEN highway_val IN ('secondary') THEN -3
            WHEN aeroway_val IN ('runway') THEN -3
            WHEN aeroway_val IN ('taxiway') THEN -3.5
            WHEN highway_val IN ('tertiary') THEN -4
            WHEN highway_val LIKE '%_link' THEN -5
            WHEN highway_val IN ('residential', 'unclassified', 'road') THEN -6
            WHEN highway_val IN ('unclassified', 'service', 'minor') THEN -7
            WHEN railway_val IN ('subway') THEN -8
            ELSE -9 END)
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_is_water(
    waterway_val text, natural_val text, landuse_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (
        waterway_val IN ('riverbank', 'dock')
     OR natural_val IN ('water')
     OR landuse_val IN ('basin', 'reservoir')
    );
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_calculate_is_building_or_part(
    building_val text, buildingpart_val text)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (building_val IS NOT NULL OR buildingpart_val IS NOT NULL);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- functions to temporarily enable and disable triggers
-- prevents them from firing while executing mass updates

CREATE OR REPLACE FUNCTION mz_tables_with_triggers()
RETURNS TEXT[] AS $$
BEGIN
    RETURN ARRAY['planet_osm_polygon', 'planet_osm_line', 'planet_osm_point', 'water_polygons'];
END;
$$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION mz_disable_triggers()
RETURNS VOID AS $$
DECLARE table_name TEXT;
BEGIN
    FOREACH table_name IN ARRAY mz_tables_with_triggers()
    LOOP
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' DISABLE TRIGGER USER';
    END LOOP;
END;
$$ LANGUAGE plpgsql VOLATILE;

CREATE OR REPLACE FUNCTION mz_enable_triggers()
RETURNS VOID AS $$
DECLARE table_name TEXT;
BEGIN
    FOREACH table_name IN ARRAY mz_tables_with_triggers()
    LOOP
        EXECUTE 'ALTER TABLE ' || quote_ident(table_name) ||
                ' ENABLE TRIGGER USER';
    END LOOP;
END;
$$ LANGUAGE plpgsql VOLATILE;
