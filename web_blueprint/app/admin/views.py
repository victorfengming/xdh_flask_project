from . import admin
from flask import render_template,jsonify,request,url_for
from app.models import Model

import time,random,datetime
from app import app
import urllib
import urllib.request
import json


# 后台首页
@admin.route("/")
def index():
    return render_template('index.html')


# 图书列表
@admin.route("/books/index")
def books_index():
    # 获取当前所有的图书信息
    data = Model().query('select * from books')
    # 加载模板  分配数据
    return render_template('books/index.html',books=data)

#图书的添加
@admin.route('/books/add',methods=['GET','POST'])
def books_add():
    # 判断当前的请求方式
    if request.method == 'GET':
        # 显示添加的表单
        return render_template('books/add.html')
    else:
        # 接受表单数据
        data = request.form.to_dict()
        # print(data)

        # 判断是否上传了封面图
        myfile = request.files.get('pic')
        # print(app.config['UP_DIR'])
        if myfile :
            # 执行文件的上传操作
            Suffix = myfile.filename.split('.').pop() # 1.jpg
            filename = str(time.time())+str(random.randint(10000,99999))+'.'+Suffix
            myfile.save(app.config["UP_DIR"]+ filename)
            data['pic_url'] = filename
        else:
            # 判断是否右隐藏域传递了豆瓣的远程图片
            imgurl = request.form.get('doubanimage',None)
            if not imgurl:
                return '<script>alert("请选择图书的封面图");history.back(-1);</script>'

            # 把远程的图片下载到本地服务器中 存储
            Suffix = imgurl.split('.').pop()
            filename = str(time.time())+str(random.randint(10000,99999))+'.'+Suffix
            urllib.request.urlretrieve(imgurl,app.config["UP_DIR"]+filename)
            data['pic_url'] = filename
            data.pop('doubanimage')
        # return ''

        data['addtime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 执行数据的添加
        sql = '''
        insert into books values(
        null,"{title}","{author}","{pic_url}"
        ,"{price}","{publisher}","{isbn13}","{summary}"
        ,"{catalog}","{pubdate}","{author_intro}"
        ,"{status}","{num}","{addtime}"
        )
        '''.format(**data)
        res = Model().exec(sql)
        print(sql)
        print(res)
        if res :
            return '<script>alert("添加成功");location.href="'+url_for('admin.books_index')+'"</script>'
        
        return '<script>alert("添加失败");location.href="'+url_for('admin.books_add')+'"</script>'



#isbn13书籍查询
@admin.route('/books/search')
def books_search():
    
    # 接收书号
    isbn13 = request.args.get('isbn13')


    # 向豆瓣发起请求,获取书籍信息
    req = urllib.request.urlopen(
        url= 'https://api.douban.com/v2/book/isbn/'+isbn13,
    )
    # 获取接口响应的内容
    content = req.read()
    res = json.loads(content.decode('utf-8'))
    # print(res)
    return jsonify(res)
