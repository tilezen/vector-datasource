DO $$
BEGIN

IF NOT EXISTS (
  SELECT 1 FROM pg_attribute
    WHERE attrelid = 'public.wof_neighbourhood'::regclass
    AND attname = 'l10n_name'
    AND NOT attisdropped) THEN

  ALTER TABLE wof_neighbourhood ADD COLUMN l10n_name HSTORE;
END IF;

END $$;
