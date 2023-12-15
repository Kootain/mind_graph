import uuid

from flask import jsonify, request
from ..api import api
from PIL import Image, ImageDraw, ImageFont
from urllib.parse import urljoin
from .visit import keywords
from ..service.graph_service import GraphService
from ..util.graph import Keyword, Connection, draw

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

    nodes = {}
    edges = {}
    for r in ret:
        from_node = r.objects[0]
        for sub in [r.objects[i:i + 2] for i in range(1, len(r.objects), 2)]:
            # print(sub)
            (edge, to_node) = sub
            if from_node.id not in nodes:
                nodes[from_node.id] = Keyword(from_node.id)
                print(f"from node id {from_node.id}")
            if to_node.id not in nodes:
                nodes[to_node.id] = Keyword(to_node.id)
                print(f"to node id {to_node.id}")

            if from_node.id == to_node.id:
                continue

            key = f"{from_node.id}#{to_node.id}"
            if key not in edges:
                edges[key] = Connection(from_keyword=from_node, to_keyword=to_node)
                print(f"edge id {key}")

    filename = str(uuid.uuid1())
    img_path = f'app/static/img/{filename}.png'

    draw(list(nodes.values()), list(edges.values()), img_path)

    url = urljoin(request.url_root, f'/static/img/{filename}.png')
    resp["url"] = url

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
