CREATE INDEX
  planet_osm_polygon_geom_min_zoom_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_boundary_min_zoom IS NOT NULL OR
    mz_building_min_zoom IS NOT NULL OR
    mz_earth_min_zoom IS NOT NULL OR
    mz_landuse_min_zoom IS NOT NULL OR
    mz_poi_min_zoom IS NOT NULL OR
    mz_transit_level IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;
