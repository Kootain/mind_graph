from app.service.base_service import BaseGraphService
from gremlin_python.driver import client
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
import os

username = os.getenv('gdb_username')
password = os.getenv('gdb_password')
host = 'gds-t4n023gomp5sfjyj81850pub.graphdb.singapore.rds.aliyuncs.com'
port = '3734'
client = client.Client(f'ws://{host}:{port}/gremlin', 'g', username=username, password=password)
conn = DriverRemoteConnection(f'ws://{host}:{port}/gremlin', 'g', username=username, password=password)


def call(q):
    callback = client.submit(q).all().result()
    for result in callback:
        print(result)


class GraphService(BaseGraphService):
    def __init__(self):
        graph = traversal().withRemote(conn)

    def add_edge(self, from_node, to_node):
        # 建立点, 点类型 gdb_sample_person, 属性 {id, name}
        create_points_edge = [
            "g.addV('mind_keyword').property(id, '{}')".format(from_node),
            "g.addV('mind_keyword').property(id, '{}')".format(to_node),
            "g.V().has('id', '{}').addE('links').to(g.V().has('id', '{}'))".format(from_node, to_node),
        ]
        for g in create_points_edge:
            print(g)
            call(g)

    def remove_edge(self, from_node, to_node):
        raise NotImplementedError()

    def get_sub_graph(self, center_node):
        raise NotImplementedError()

    def get_node(self, node):
        raise NotImplementedError()
