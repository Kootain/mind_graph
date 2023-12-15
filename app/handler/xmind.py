import uuid

from flask import jsonify, request
from ..api import api
from PIL import Image, ImageDraw, ImageFont
from urllib.parse import urljoin
from .visit import keywords
from ..service.graph_service import GraphService

graph_service = GraphService()


@api.get('/xmind')
def xmind():
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

    ret = graph_service.get_sub_graph(keyword)
    if not ret:
        resp['suc'] = False
        resp["reason"] = "keyword does not exist"
        return resp

    # parser for sub-graph

    return jsonify(resp)


def test_mind():
    # 制图
    image = Image.new('RGB', (200, 200), color=(73, 109, 137))
    d = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    d.text((80, 80), ','.join(keywords), fill=(0, 0, 0), font=font)
    # 存图
    filename = str(uuid.uuid1())
    img_path = f'app/static/img/{filename}.jpg'
    image.save(img_path)
    url = urljoin(request.url_root, f'/static/img/{filename}.jpg')
    return jsonify({"imageUrl": url})
