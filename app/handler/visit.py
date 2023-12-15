# coding=utf-8
from flask import jsonify, request
from ..api import api
import random

keywords = ['python', 'mysql']


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
    random.shuffle(next_keywords)
    return jsonify({'suc': True, 'sorted_keywords': next_keywords})


@api.get('/keyword')
def keyword():
    return jsonify(keywords)