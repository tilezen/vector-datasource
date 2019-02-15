-- polygon zoom 7 specific query
CREATE INDEX
  planet_osm_polygon_geom_min_zoom_8_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_earth_min_zoom < 8 OR
    mz_landuse_min_zoom < 8 OR
    mz_poi_min_zoom < 8 OR
    mz_transit_level < 8;
