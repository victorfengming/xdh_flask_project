from flask import Flask

app = Flask(__name__)
app.debug = True

from app.api import api as api_blueprint
from app.admin import admin as admin_blueprint


# 注册蓝图
app.register_blueprint(api_blueprint,url_prefix="/api")
app.register_blueprint(admin_blueprint)