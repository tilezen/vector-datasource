UPDATE planet_osm_polygon SET
  mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE
    "disused" <> 'no' OR
    "railway" = 'station';

CREATE INDEX new_planet_osm_polygon_landuse_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 9;
CREATE INDEX new_planet_osm_polygon_landuse_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 12;
CREATE INDEX new_planet_osm_polygon_landuse_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 15;

CREATE INDEX new_planet_osm_polygon_landuse_boundary_geom_4_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom IS NOT NULL AND (boundary IN ('national_park', 'protected_area') OR leisure='nature_reserve') AND mz_landuse_min_zoom <= 4;
CREATE INDEX new_planet_osm_polygon_landuse_boundary_geom_6_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom IS NOT NULL AND (boundary IN ('national_park', 'protected_area') OR leisure='nature_reserve') AND mz_landuse_min_zoom <= 6;
CREATE INDEX new_planet_osm_polygon_landuse_boundary_geom_8_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom IS NOT NULL AND (boundary IN ('national_park', 'protected_area') OR leisure='nature_reserve') AND mz_landuse_min_zoom <= 8;

ANALYZE planet_osm_polygon;
