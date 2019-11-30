from . import admin
from flask import render_template, jsonify, request
from app.models import Model
# 后台首页
@admin.route("/")
def index():
    return render_template('index.html')

# 图书列表
@admin.route("/books/index")
def books_index():

    res = Model().query('select * from user')
    print(res)

    # return jsonify(res)
    return render_template("book/index.html")

# 图书的添加
@admin.route('/books/add',methods=['GET','POST'])
def books_add():
    # 在这里一个 视图函数就都能搞定了
    # 判断当前的请求方式
    if request.method == 'GET':
        # xianshixian显示添加的表单
        return render_template("book/add.html")

