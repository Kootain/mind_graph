from flask import jsonify, request
from ..api import api
from ..service.graph_service import GraphService
from gremlin_python.structure.graph  import Vertex

graph_service = GraphService()


@api.get('/keyword')
def keyword():
    keyword = request.args.get('keyword')
    resp = {
        "input": keyword,
        'suc': True,
        "reason": ""
    }
    # retrieve the specified keyword from graph
    ret = graph_service.get_node(keyword)
    if not ret:
        resp['suc'] = False
        resp["reason"] = "ret is empty"
        return resp

    resp['element'] = ret[0].__format__()
    
    return jsonify(resp)
