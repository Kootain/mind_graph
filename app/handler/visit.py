# coding=utf-8
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
    if current_keyword:
        keywords.append(current_keyword)
    if next_keywords:
        keywords.extend(next_keywords)
    print(current_keyword, next_keywords)
    graph_service.add_edge(current_keyword, next_keywords[0])
    return jsonify({'suc': True})


@api.get('/keyword')
def keyword():
    keyword = request.args.get('keyword')
    # retrieve the specified keyword from graph
    graph_service.get_node(keyword)
    return jsonify(keywords)