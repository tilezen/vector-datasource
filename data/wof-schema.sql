CREATE TABLE wof_neighbourhood (
  wof_id BIGINT UNIQUE NOT NULL,
  placetype SMALLINT NOT NULL,
  name TEXT NOT NULL,
  hash TEXT NOT NULL,
  n_photos INTEGER,
  area BIGINT,
  label_position geometry(Point, 900913) NOT NULL,
  geometry geometry(Geometry, 900913) NOT NULL
);

CREATE INDEX wof_neighbourhood_wof_id_index ON wof_neighbourhood(wof_id);
CREATE INDEX wof_neighbourhood_label_position_index ON wof_neighbourhood USING GIST(label_position);
CREATE INDEX wof_neighbourhood_geometry_index ON wof_neighbourhood USING GIST(geometry);

CREATE TABLE wof_neighbourhood_placetype (
  placetype_code SMALLINT UNIQUE NOT NULL,
  placetype_string text NOT NULL
);

INSERT INTO wof_neighbourhood_placetype VALUES
  (1, 'neighbourhood'),
  (2, 'microhood'),
  (3, 'macrohood');
