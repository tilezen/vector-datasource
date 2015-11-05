CREATE TABLE wof_neighbourhood_placetype (
  placetype_code SMALLINT PRIMARY KEY,
  placetype_string text NOT NULL
);

INSERT INTO wof_neighbourhood_placetype VALUES
  (1, 'neighbourhood'),
  (2, 'microhood'),
  (3, 'macrohood');

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
  geometry geometry(Geometry, 900913) NOT NULL
);

CREATE INDEX wof_neighbourhood_label_position_index ON wof_neighbourhood USING GIST(label_position);
CREATE INDEX wof_neighbourhood_min_zoom_index ON wof_neighbourhood(min_zoom);
CREATE INDEX wof_neighbourhood_max_zoom_index ON wof_neighbourhood(max_zoom);
