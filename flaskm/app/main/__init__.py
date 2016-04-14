from flask import Blueprint 
from ..models import Permission
main = Blueprint('main', __name__)  # 实例化一个 Blueprint 类对象

@main.app_context_processor
def inject_permissions():
    # ? 上下文处理器，让变量在模板中全局可以访问
    return dict(Permission = Permission)

from . import views, errors 
#这些模块在 app/main/__init__.py 脚本的末尾导入，这是为了避免循环导入依赖，因为在views.py 和 errors.py 中还要导入蓝本 main。