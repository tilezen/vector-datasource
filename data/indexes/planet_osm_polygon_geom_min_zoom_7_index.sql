-- polygon low zoom
CREATE INDEX
  planet_osm_polygon_geom_min_zoom_7_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_landuse_min_zoom < 7 OR
    mz_poi_min_zoom < 7 OR
    mz_transit_level < 7;
