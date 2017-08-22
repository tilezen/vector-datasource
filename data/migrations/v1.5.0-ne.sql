UPDATE ne_50m_urban_areas t
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(t.*)
  WHERE COALESCE(mz_calculate_min_zoom_landuse(t.*), 999) <> COALESCE(mz_landuse_min_zoom, 999);

UPDATE ne_10m_urban_areas t
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(t.*)
  WHERE COALESCE(mz_calculate_min_zoom_landuse(t.*), 999) <> COALESCE(mz_landuse_min_zoom, 999);
