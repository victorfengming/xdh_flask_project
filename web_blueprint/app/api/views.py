import datetime
import json

from flask import jsonify, request

import app
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

#
@api.route("/register")
def register():
    # 获取code
    code = request.args.get('code')
    # 向微信服务器发请求 获取openid
    # 向微信服务器发请求,
    wxurl = '''
    https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}
    '''.format(APPID=app.config['APPID'],SECRET=app.config['SECRET'],)
    # 判断openid 是否 存在,存在更新,不存在添加
    # 接收数据
    data = request.args.to_dict()
    print(data)
    print('-'*50)
    '''
    {'code': '043mFDDu03NYIi1aPPBu0IqFDu0mFDDH', 'method': 'POST', 'userinfo': '{"username":"小萌芽","phone":"13940206091","bumen":"xdh","nikeName":"Victor","avatarUrl":"https://wx.qlogo.cn/mmopen/vi_32/iaIzMeic5IhT1mSy3uccEjHNyy30KrsXXIlCtTj3KRBiaXgz2CJ13EIAsia7Bx8WQT83u7g0iadEibTOicPZ0z46DK9ow/132"}'}

    '''
    # data['userinfo'] 是字符串格式,需要抓换类型
    user_info_data = json.loads(data['userinfo'])

    user_info_data['addtime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(user_info_data)
    print('-'*50)

    # 执行数据的添加
    sql = '''
        insert into users values(
        null,
        "{nikeName}",
        "{avatarUrl}",
        "{username}",
        "{bumen}",
        "{phone}",
        "{addtime}")
        '''.format(**user_info_data)
    # '''
    # TODO 这里可能会遇到SQL中有引号问题(SQL注入)
    # 解决方案:SQL预处理,SQL参数绑定
    print(sql)

    userid = Model().exec(sql)
    print('-'*50)
    print(userid)
    print('-'*50)
    return jsonify({'code':userid,'msg':'成功!'})
    # 我们返回 id
    # return jsonify({'code':id})
    # 这里有问题了,你执行完之后怎么拿id



