# Improving performance

Performance doesn't matter much for creating tiles for an extract, but when handling production loads for the entire planet, some thought needs to be given to it

## PostgreSQL

Entire [books](https://www.packtpub.com/big-data-and-business-intelligence/postgresql-high-performance-second-edition) have been written on tuning PostgreSQL. In general, the Tilezen database load is most similar to a Data Warehouse usecase. Look for optimization advice for large databases and ETL workloads, not OLTP ones.

General advice applicable to osm2pgsql rendering should be applicable here, including raster-based rendering. The queries are similar enough.

### Tuning

The following tunables are based on experience on dedicated SSD-based servers with at least 64GB of RAM, and RDS. They are framed as [`ALTER SYSTEM`](https://www.postgresql.org/docs/current/static/sql-altersystem.html) commands, but in production environments it is better to put the settings into your configuration management software.

```sql
-- For systems with <64GB of RAM, the memory values might need to be scaled down
ALTER SYSTEM SET effective_cache_size = 56GB;
ALTER SYSTEM SET shared_buffers = 16GB;

-- The workload involves big queries, but not hundreds of them
ALTER SYSTEM SET work_mem = 128MB;
-- osm2pgsql builds big indexes and vector-datasource also has some custom ones
ALTER SYSTEM SET maintenance_work_mem = 4GB;

-- There can be autovacuum_max_workers running at once, parallel to everything else
ALTER SYSTEM SET autovacuum_work_mem = 1GB;

-- SSDs are fast on random.
ALTER SYSTEM SET random_page_cost = 1.2;

-- The default settings won't run autovacuum nearly enough, leading to months between runs
ALTER SYSTEM SET autovacuum_vacuum_scale_factor = 0.05;
ALTER SYSTEM SET autovacuum_analyze_scale_factor = 0.02;
```
