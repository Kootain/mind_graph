# coding=utf-8
import pkgutil


def register_blueprints(api_blueprint):
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        # 根据 module_name 构造完整的模块路径
        full_module_name = f"{__name__}.{module_name}"
        # 动态导入模块
        __import__(full_module_name)
