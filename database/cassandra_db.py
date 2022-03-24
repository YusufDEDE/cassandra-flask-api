from cassandra.cluster import Cluster


class CassandraDB:
    __session = None

    def __init__(self, address: list):
        self.address: list = address
        self.__connect()

    def __connect(self):
        cluster = Cluster(contact_points=self.address)
        self.__session = cluster.connect()

    def execute_query(self, query: str = "SELECT * FROM system.local;"):
        return self.__session.execute(query=query)
