-- wof

CREATE TABLE wof_neighbourhood_placetype (
  placetype_code SMALLINT PRIMARY KEY,
  placetype_string text NOT NULL
);

INSERT INTO wof_neighbourhood_placetype VALUES
  (1, 'neighbourhood'),
  (2, 'microhood'),
  (3, 'macrohood'),
  (4, 'borough');

CREATE TABLE wof_neighbourhood (
  wof_id BIGINT PRIMARY KEY,
  placetype SMALLINT NOT NULL REFERENCES wof_neighbourhood_placetype(placetype_code),
  name TEXT NOT NULL,
  hash TEXT NOT NULL,
  n_photos INTEGER,
  area BIGINT,
  min_zoom SMALLINT NOT NULL,
  max_zoom SMALLINT NOT NULL,
  is_landuse_aoi BOOLEAN,
  label_position geometry(Point, 900913) NOT NULL,
  geometry geometry(Geometry, 900913) NOT NULL,
  inception DATE NOT NULL DEFAULT '0001-01-01',
  cessation DATE NOT NULL DEFAULT '9999-12-31',
  is_visible BOOLEAN NOT NULL DEFAULT true,
  l10n_name HSTORE
);

CREATE INDEX wof_neighbourhood_label_position_index ON wof_neighbourhood USING GIST(label_position);
CREATE INDEX wof_neighbourhood_min_zoom_index ON wof_neighbourhood(min_zoom);
CREATE INDEX wof_neighbourhood_max_zoom_index ON wof_neighbourhood(max_zoom);

-- track way ids to update from trigger

CREATE TABLE mz_pending_path_major_route (
  osm_id BIGINT NOT NULL
);
