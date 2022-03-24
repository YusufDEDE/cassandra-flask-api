import time

from database.cassandra_db import CassandraDB

CREATE_TABLE_QUERY = """
CREATE TABLE kong.users (
  userid text PRIMARY KEY,
  first_name text,
  last_name text,
  emails set<text>,
  top_scores list<int>,
  todo map<timestamp, text>
);
"""

INSERT_QUERY = """
INSERT INTO kong.users (userid, first_name, last_name, emails)
  VALUES('frodo', 'Frodo', 'Baggins', {'f@baggins.com', 'baggins@gmail.com'});
"""

SELECT_QUERY = """
SELECT * FROM kong.users;
"""

if __name__ == '__main__':
    start_time = time.perf_counter()

    cassandra_db = CassandraDB(address=['localhost', ])
    res = cassandra_db.execute_query(query=SELECT_QUERY)

    print(res.all())

    finish_time = time.perf_counter()
    print(f"Finished in {round(finish_time - start_time, 2)} seconds..")
