CREATE TABLE wof_neighbourhood (
  wof_id BIGINT UNIQUE,
  name TEXT NOT NULL
);

SELECT AddGeometryColumn ('wof_neighbourhood', 'label_position', 900913, 'POINT', 2);

CREATE INDEX wof_neighbourhood_label_position_index ON wof_neighbourhood USING GIST(label_position);
