from flask import jsonify, request
from ..api import api
from ..service.graph_service import GraphService

graph_service = GraphService()


@api.get('/edge')
def edge():
    from_node = request.args.get('from_node')
    to_node = request.args.get('to_node')
    resp = {
        "from_node": from_node,
        "to_node": to_node,
        'suc': True,
        "reason": "",
        "ele": []
    }
    # retrieve the specified edge from graph
    ret = graph_service.get_edge(from_node, to_node)
    if not ret:
        resp['suc'] = False
        resp["reason"] = "edge does not exist"
        return resp

    for ele in ret:
        resp['ele'].append(
            {
                "id": ele.id,
                "label": ele.label,
                "properties": ele.properties
            })

    return jsonify(resp)
