# app/__init__.py

from flask import Flask


def create_app(config_filename=None):
    app = Flask(__name__, static_folder='static')

    # 配置应用
    if config_filename:
        app.config.from_pyfile(config_filename)

    # 初始化数据库
    # from .models import db
    # db.init_app(app)

    # 注册蓝图
    from .views import main
    from .api import api
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    # 可以添加更多的初始化代码，如设置日志、认证系统、缓存系统等

    return app
