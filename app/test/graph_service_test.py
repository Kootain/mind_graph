import unittest
from app.service.graph_service import GraphService


class TestGraphService(unittest.TestCase):
    def __init__(self):
        super().__init__()

    def test_get_node(self):
        keyword = 'Chinese'
        graph_service = GraphService()
        ret = graph_service.get_node(keyword)
        print(ret)
