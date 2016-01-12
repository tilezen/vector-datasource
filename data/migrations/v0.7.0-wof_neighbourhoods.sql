-- need to add the inception and cessation columns to handle
-- neighbourhood lifetime. we default these to:
--   '0001-01-01' for inception and
--   '9999-12-31' for cessation
-- because these are the earliest/latest dates for an EDTF
-- 'uuuu' format time, which is what we default to when the
-- WOF neighbourhood doesn't specify what time it actually
-- wants.
--
-- futher, we add a "visible now" column which is updated
-- by running the
DO $$
BEGIN

IF NOT EXISTS (
  SELECT 1
  FROM   pg_attribute
  WHERE  attrelid = 'wof_neighbourhood'::regclass
  AND    attname = 'inception'
  AND    NOT attisdropped
  ) THEN

  ALTER TABLE wof_neighbourhood
    ADD COLUMN inception DATE NOT NULL DEFAULT '0001-01-01',
    ADD COLUMN cessation DATE NOT NULL DEFAULT '9999-12-31',
    ADD COLUMN is_visible BOOLEAN NOT NULL DEFAULT true;
END IF;

END$$;
