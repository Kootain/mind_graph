# coding = utf-8
from flask import Blueprint, jsonify, request
from PIL import Image

api = Blueprint('api', __name__)

from .handler import register_blueprints
register_blueprints(api)

keywords = []


