from flask import jsonify, request

from . import api
from app.models import Model


#
@api.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"


#
@api.route("/list")
def books_list():
    # 获取关键字
    keywords = request.args.get('keywords', None)
    if keywords:
        print("有keywords:")
        print(keywords)
        # 搜素书籍信息
        data = Model().query('select * from wxapp.books where title like "' + keywords + '"')
    else:
        # 获取当前所有书籍信息,并返回json数据
        data = Model().query('select * from wxapp.books')
        print(data)

    return jsonify(data)
