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

    def add_edge(self, from_node, to_node_ar):
        # from node
        add_edge_commands = [f"g.V ().coalesce (g.V ().has (id, '{from_node}'),g.addV ().property (id, '{from_node}'))"]

        # to node array
        for to_node in to_node_ar:
            add_edge_commands.append(
                f"g.V ().coalesce (g.V ().has (id, '{to_node}'),g.addV ().property (id, '{to_node}'))"
            )

            # 判断顶点是否存在，如果不存在则插入
            add_edge_commands.append(
                f"g.V().has(id, '{from_node}'). as ('a').V().has(id, '{to_node}'). as ('b').coalesce("
                "__.inE().where(outV(). as ('a')).where(inV(). as ('b')),"
                "__.addE('links').from('a').to('b').property('weight', 0)"
                ").as ('e').values('weight'). as ('v').select('e').property('weight', math('v + 1'))"
            )

        for g in add_edge_commands:
            call(g)

    def remove_edge(self, from_node, to_node):
        raise NotImplementedError()

    def get_sub_graph(self, center_node):
        raise NotImplementedError()

    def get_node(self, node):
        raise NotImplementedError()
