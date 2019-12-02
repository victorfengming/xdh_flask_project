from flask import jsonify

from . import api
from app.models import Model


#
@api.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"

#
@api.route("/list")
def books_list():
    # 获取当前所有书籍信息,并返回json数据
    data = Model().query('select * from wxapp.books')
    print(data)

    return jsonify(data)

