# Sharding  DB Indexing

With sharing it’s difficult to know which partition the target records are except we scan each partition and each record.
It’s easy to make a hash map of ID to know exactly where is the specific row with given ID, but it doesn’t work if we query more columns.
The combination of multiple columns can be “infinite” and we cannot make infinite index.

BUT, I think the query statement is not infinite most of the time. For production programs, the SQL patterns are written in the code which aren’t changed very often.
Since that number of query pattern is stable and controllable, we can build hashing index to each query patterns.

If the DB server see the filter “where a in (1,2,3) and b = 0”, it will seek the existing index for “a, b” to know exactly where are the target records located.
If the index does not exist, the server should just run the scan anyway to build a new index for this query pattern.
While any new record is written into DB, the server should update each existing index.

So the problem is these index can be also taking a lot of spaces, but we still think that’s not growing as fast as the records themselves, and much easier to handle.

We need a SQL proxy to accept any normal SQL statement and DB connection, like RDS Proxy. And what it does is to search the index and get the target sharding locations, then rewrite the SQL and send actual queues concurrently to each sharding server. Then concatenation the result records.
The benefit of proxy server helps on both sharding query and connection pool.
