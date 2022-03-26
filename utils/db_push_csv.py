import pandas as pd
import concurrent.futures
from database.cassandra_db import CassandraDB
from utils.helper import generate_query_with_df_column


class DBPushCSV(CassandraDB):
    def __init__(self, **kwargs):
        self.address: list = kwargs.get('address', ['localhost', ])
        self.csv_path: str = kwargs.get('csv_path', '')
        self.column_names: list = kwargs.get('column_names', [])
        super(DBPushCSV, self).__init__(address=self.address)

    def get_csv_data(self):
        df = pd.read_csv(filepath_or_buffer=self.csv_path, sep=',', names=self.column_names)
        return df

    def push_db(self, db_name: str):
        df = self.get_csv_data()
        # query = generate_query_with_df_column(
        #     columns=self.column_names,
        #     db_name=db_name
        # )

        index = 1

        query: str = "INSERT INTO amazon_review (id, polarity, title, text) VALUES " \
                     "(%(id)s, %(polarity)s, %(title)s, %(text)s)"

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for dt in df.to_dict("records"):
                data: dict = {
                    "id": str(index),
                    "polarity": str(dt.get('polarity')),
                    "title": str(dt.get('title')),
                    "text": str(dt.get('text'))
                }
                executor.submit(self.execute_query, query, data)
                index += 1
