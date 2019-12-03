from flask import Flask
import os

app = Flask(__name__)
app.debug = True


from app.api import api as api_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(admin_blueprint)
app.register_blueprint(api_blueprint,url_prefix="/api")

# 上传文件配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# /home/yc/py16/18-flask/web

app.config['UP_DIR'] = BASE_DIR+'/app/static/uploads/'

# 小程序的配置
app.config['APPID'] = 'wxaa593d1b99bf0198'
app.config['SECRET'] = '70c8318ee9efef3d1ecda53cf31199b9'
