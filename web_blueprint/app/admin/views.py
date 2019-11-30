import datetime
import random
import time

from app import app
from . import admin
from flask import render_template, jsonify, request, url_for
from app.models import Model


# 后台首页
@admin.route("/")
def index():
    return render_template('index.html')


# 图书列表
@admin.route("/books/index")
def books_index():
    res = Model().query('select * from wxapp.books')
    print(res)

    # return jsonify(res)
    return render_template("book/index.html")


# 图书的添加
@admin.route('/books/add', methods=['GET', 'POST'])
def books_add():
    # 在这里一个 视图函数就都能搞定了
    # 判断当前的请求方式
    if request.method == 'GET':
        # xianshixian显示添加的表单
        return render_template("book/add.html")
    else:
        # 接受表单数据
        data = request.form
        print(data)
        # flask提供了一个方法
        # 能直接将data转换成dict,
        data = data.to_dict()
        # 判断是否上传了封面图
        myfile = request.files.get('pic')
        print(myfile)
        if myfile:
            # 执行文件的上传操作
            Suffix = myfile.filename.split('.').pop()
            filename = str(time.time())+str(random.randint(10000,99999))+'.'+Suffix
            myfile.save(app.config["UP_DIR"]+filename)
            print(app.config["UP_DIR"] + filename)
            # 把图片加到data中
            data['pic_url'] = filename
            print('-'*80)
            print(data)
            print('-'*80)

        # 日期
        data['addtime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 执行数据的添加
        sql = '''
        insert into books values(
            null,
            "{title}",
            "{author}",
            "{pic_url}",
            "{publisher}",
            "{price}",
            "{isbn13}",
            "{summary}",
            "{catalog}",
            "{author_intro}",
            "{pubdate}",
            "{status}",
            "{num}",
            "{addtime}"
        )
        '''.format(**data)

        print(sql)
        res = Model().exec(sql)
        if res:
            return '<script>alert("添加成功");location.href="'+url_for('admin.books_index')+'"</script>'
        else:
            return '<script>alert("添加失败");location.href="'+url_for('admin.books_index')+'"</script>'


        return render_template("book/add.html")
