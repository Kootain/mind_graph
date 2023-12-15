from flask import jsonify, request
from ..api import api


# curl -v -X POST http://127.0.0.1:5000/api/ping\?query=test -d '{"a":1}' -H 'Content-type: application/json'
@api.post('/ping')
def ping():
    resp = {
        'pong': {
            'query': request.args.get('query', default='1', type=str),
            'body': request.json,
        }
    }
    return jsonify(resp)
