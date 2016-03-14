DO $$
BEGIN
-- drop this function if it exists - postgres doesn't like CREATE OR REPLACE
-- where the type is changing to include IN/OUT parameters, as internally the
-- OUT parameters only affect the return type, and changing that isn't
-- permitted.
--
IF EXISTS(SELECT * FROM pg_proc WHERE
    proname = 'mz_calculate_transit_routes' AND
    pg_get_function_arguments(oid) = 'bigint, bigint') THEN
  DROP FUNCTION mz_calculate_transit_routes(bigint,bigint);
END IF;
END$$;
