from cassandra.cluster import Cluster


class CassandraDB:
    __session = None
    __prepared: str = ""

    def __init__(self, address: list):
        self.address: list = address
        self.__connect()

    def __connect(self):
        cluster = Cluster(contact_points=self.address)
        self.__session = cluster.connect('kong')

    def execute_query(self, query: str, data: dict = None):
        _query = query

        if data:
            _query = query, data

        return self.__session.execute(_query)
