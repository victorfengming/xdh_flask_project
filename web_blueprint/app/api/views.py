from . import api
from flask import jsonify,request
from app.models import Model
from app import app

import datetime,json
import urllib
import urllib.request

@api.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"

@api.route("/list")
def books_list():

    # 获取关键字
    keywords = request.args.get('keywords',None)
    if keywords:
        # 搜索书籍信息
        data = Model().query('select * from books where title like "%'+keywords+'%"')
    else:
        # 获取当前所有书籍信息,并返回json数据
        data = Model().query('select * from books')
    return jsonify(data)


@api.route("/register",methods=['GET','POST'])
def register():
    
    # 获取 code  
    code = request.args.get('code')
    # 向微信服务器发请求 获取 openid
    # GET 
    wxurl = '''
    https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code
    '''.format(APPID=app.config['APPID'],SECRET=app.config['SECRET'],JSCODE=code)
    # 向微信服务器发起请求,获取openid
    req = urllib.request.urlopen(
        url= wxurl
    )
    # 获取接口响应的内容
    content = req.read()
    resdata = json.loads(content.decode('utf-8'))

    # {'session_key': 'B4RnIIYNQNPa3+hCWexeYg==', 
    # 'openid': 'oo-ye4riGgJLZzdLA6cZu-3f8o-E'}

    # 判断openid是否存在
    sql = 'select * from users where openid="{}"'.format(resdata['openid'])
    fromres = Model().query(sql)
    if fromres:
        # 存在,则返回
        return jsonify({'msg':'用户已经存在','code':fromres[0]['id']})
  
    # 不存在,则添加
    # 接收数据
    userdata = json.loads(request.args.get('userinfo'))
    userdata['openid'] =  resdata['openid']
    # 设置注册时间
    userdata['addtime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 执行数据的添加
    sql = '''
        insert into users values(
        null,"{nikeName}","{avatarUrl}",
        "{username}","{bumen}","{phone}",
        "{openid}","{addtime}")
        '''.format(**userdata)
    # 执行添加,并获取最后的id
    userid = Model().exec(sql)
    # 返回json数据
    return jsonify({'code':userid,'msg':'ok'})



# 图书借阅
@api.route('/books/borrow')
def books_borrow():
    # 接受数据
    data = request.args.to_dict()

    # 先检测当前图书的数量
    selsql = 'select num from books where isbn13 = '+data['book_isbn']
    selres = Model().query(selsql)
    if selres[0]['num'] <= 0:
        return jsonify({'msg':'当前图书已经被借阅,只能预约','error':1})

    data['addtime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['status'] = 0
    # 执行数据的创建
    sql = 'insert into borrow values(null,"{book_isbn}",{user_id},"{addtime}",{status})'.format(**data)

    # # 修改图书的可借阅的数量
    upsql = 'update books set num = num-1 where isbn13 = '+data['book_isbn']

    import pymysql     
    # 打开数据库连接
    db = pymysql.connect("localhost","root","123456","wxapp" )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    try:
        # 执行sql语句
        cursor.execute(sql)
        cursor.execute(upsql)
        # 提交到数据库执行
        db.commit()
        resdata = {'msg':'ok','error':0}
    except:
        # 如果发生错误则回滚
        db.rollback()
        resdata = {'msg':'执行错误','error':2}
     
    # 关闭数据库连接
    db.close()

    return jsonify(resdata)

# 获取当前用户的借阅信息
@api.route('/get/borrow')
def get_borrow():
    # 获取用户id
    userid = request.args.get('userid')
    # 获取当前用户的借阅信息
    sql = 'select bw.*,books.title,books.pic_url,books.author,books.price,books.publisher from borrow as bw inner join books on bw.book_isbn = books.isbn13 where bw.user_id = {user_id}'.format(user_id=userid)
    res = Model().query(sql)
    return jsonify(res)


