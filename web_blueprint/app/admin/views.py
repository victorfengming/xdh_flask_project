from . import admin
from flask import render_template

# 后台首页
@admin.route("/")
def index():
    return render_template('index.html')

# 图书列表
@admin.route("/books/index")
def books_index():
    return render_template("book/index.html")