import uuid

from flask import jsonify, request
from ..api import api
from ..service.graph_service import GraphService
from dataclasses import dataclass
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

    # node {"color": "#97c2fc", "id": "Python", "label": "Python", "shape": "dot"},
    # edge {"arrows": "to", "from": "Python", "to": "Java", "value": 0.5},

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
                    edges[key] = {
                        "from": from_node.id,
                        "to": to_node.id,
                    }

            if isinstance(obj, Vertex):
                if obj.id not in nodes:
                    nodes[obj.id] = {
                        "color": "#97c2fc",
                        "id": obj.id,
                        "label": obj.id,
                        "shape": "dot",
                    }
    resp['nodes'] = list(nodes.values())
    resp['edges'] = list(edges.values())
    return jsonify(resp)
