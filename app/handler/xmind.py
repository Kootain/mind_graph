import uuid

from flask import jsonify, request
from ..api import api
from PIL import Image, ImageDraw, ImageFont
from urllib.parse import urljoin
from .visit import keywords


@api.get('/xmind')
def xmind():
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