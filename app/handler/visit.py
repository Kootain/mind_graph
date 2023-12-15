# coding=utf-8
import random

from flask import jsonify, request
from ..api import api
from ..service.graph_service import GraphService

keywords = ['python', 'mysql']
graph_service = GraphService()


@api.post('/visit')
def visit():
    data = request.json
    current_keyword = data.get('current_keyword', '')
    next_keywords = data.get('next_keywords', [])
    random.shuffle(next_keywords)

    resp = {
        "current_keyword": current_keyword,
        "next_keywords": next_keywords,
        'suc': True,
        "reason": ""
    }

    if not current_keyword:
        resp['suc'] = False
        resp["reason"] = "current keyword is empty"
        return jsonify(resp)

    if not next_keywords:
        resp['suc'] = False
        resp["reason"] = "the list next keyword is empty"
        return jsonify(resp)

    graph_service.add_edge(current_keyword, next_keywords)
    return jsonify(resp)


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
    resp['data'] = ret
    #resp['keyword'] = ret['nodes']
    return jsonify(resp)