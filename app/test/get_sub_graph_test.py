import unittest
from app.service.graph_service import GraphService
class TestGetSubGraph(unittest.TestCase):
    def test_get_sub_graph(self):
        keyword = 'Language'
        graph_service = GraphService()
        ret = graph_service.get_sub_graph(keyword)

        print(ret[0])
        print(ret[0].id.__class__)
        print(ret[0].id)

        print(ret[0].label.__class__)
        print(ret[0].label)

        print(ret[0].properties.__class__)
        print(ret[0].properties)