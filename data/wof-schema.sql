CREATE TABLE wof_neighbourhood (
  wof_id BIGINT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  hash TEXT NOT NULL,
  n_photos INTEGER,
  label_position geometry(Point, 900913) NOT NULL,
  geometry geometry(Geometry, 900913) NOT NULL
);

CREATE INDEX wof_neighbourhood_wof_id_index ON wof_neighbourhood(wof_id);
CREATE INDEX wof_neighbourhood_label_position_index ON wof_neighbourhood USING GIST(label_position);
CREATE INDEX wof_neighbourhood_geometry_index ON wof_neighbourhood USING GIST(geometry);
