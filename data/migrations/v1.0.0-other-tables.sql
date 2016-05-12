DO $$
BEGIN

IF NOT EXISTS (
  SELECT 1 from wof_neighbourhood_placetype WHERE placetype_code = 4) THEN

  INSERT INTO wof_neighbourhood_placetype (placetype_code, placetype_string) VALUES (4, 'borough');
END IF;

END $$;
