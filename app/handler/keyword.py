from flask import jsonify, request
from ..api import api
from ..service.graph_service import GraphService

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
    print(ret)
    #resp['keyword'] = ret[0]['nodes']
    return jsonify(resp)