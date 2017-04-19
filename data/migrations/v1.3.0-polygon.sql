UPDATE
  planet_osm_polygon p
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(p.*),
      mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(p.*)
  WHERE
    (tags -> 'leisure' = 'garden' OR
     tags -> 'landuse' = 'village_green' OR
     tags -> 'natural' IN ('wood', 'forest') OR
     (NOT tags ? 'name' AND mz_poi_min_zoom IS NOT NULL))
    AND (
      COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(p.*), 999) OR
      COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(p.*), 999)
    );
