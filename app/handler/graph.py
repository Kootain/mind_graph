import uuid

from flask import jsonify, request
from ..api import api
from ..service.graph_service import GraphService

graph_service = GraphService()


@api.get('/graph')
def graph():
    keyword = request.args.get('keyword')
    resp = {
        "input": keyword,
        'suc': True,
        "reason": ""
    }
    if not keyword:
        resp['suc'] = False
        resp["reason"] = "keyword is empty"
        return jsonify(resp)

    nodes = {}
    edges = {}

    return jsonify({'nodes': list(nodes.values()), 'edge': list(edges.values())})
