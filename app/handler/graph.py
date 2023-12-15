import uuid

from flask import jsonify, request
from ..api import api
from ..service.graph_service import GraphService
from ..util.graph import Keyword, Connection, draw
from gremlin_python.structure.graph import Edge, Vertex

graph_service = GraphService()


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


@api.get('/graph')
def graph():
    keyword = request.args.get('keyword')
    depth = request.args.get('depth', 3)
    depth = clamp(depth, 1, 5)
    resp = {
        "input": keyword,
        "depth": depth,
        'suc': True,
        "reason": ""
    }
    if not keyword:
        resp['suc'] = False
        resp["reason"] = "keyword is empty"
        return jsonify(resp)

    ret = graph_service.get_sub_graph(keyword, depth)
    if not ret:
        resp['suc'] = False
        resp["reason"] = "keyword does not exist"
        return resp

    nodes = {}
    edges = {}
    for r in ret:
        for obj in r.objects:
            if isinstance(obj, Edge):
                from_node = obj.outV
                to_node = obj.inV

                if from_node.id == to_node.id:
                    continue

                key = f"{from_node.id}#{to_node.id}"
                if key not in edges:
                    edges[key] = Connection(from_keyword=from_node.id, to_keyword=to_node.id)

            if isinstance(obj, Vertex):
                if obj.id not in nodes:
                    nodes[obj.id] = Keyword(obj.id)

    return jsonify({'nodes': list(nodes.values()), 'edge': list(edges.values())})


