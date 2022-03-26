import time

from database.cassandra_db import CassandraDB

# CREATE KEYSPACE IF NOT EXISTS kong WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };
from utils.db_push_csv import DBPushCSV

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

CREATE_AMAZON_REVIEW_TABLE_QUERY = """
CREATE TABLE kong.amazon_review (
  id text PRIMARY KEY,
  polarity text,
  title text,
  text text,
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

    # cassandra_db = CassandraDB(address=['localhost', ])
    # res = cassandra_db.execute_query(query=CREATE_AMAZON_REVIEW_TABLE_QUERY)
    # print(res.all())

    # db_push_csv = DBPushCSV(
    #     address=['localhost', ],
    #     csv_path='amazon_review_polarity_csv/test.csv',
    #     column_names=['polarity', 'title', 'text']
    # )

    # print(db_push_csv.get_csv_data())
    # print(db_push_csv.push_db(db_name="kong.amazon_review"))

    finish_time = time.perf_counter()
    print(f"Finished in {round(finish_time - start_time, 2)} seconds..")
