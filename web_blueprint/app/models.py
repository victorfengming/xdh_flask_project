


# pymysql 
'''
    1,链接mysql数据库
    # 打开数据库连接
    db = pymysql.connect("localhost","testuser","test123","TESTDB" )


    2,创建游标对象
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    3,执行sql语句
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")

    4,返回结果 
    fetchone 获取单条结果,
    fetchall 获取所有结果
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    5,关闭链接
    # 关闭数据库连接
    db.close()
'''
import pymysql

class Model():
    # 属性
    Mysql_localhost = 'localhost'
    Mysql_username = 'root'
    Mysql_password = '123456'
    Mysql_select_DB = 'wxapp'
    Mysql_charset = 'utf8mb4'
    Mysql_cursorclass=pymysql.cursors.DictCursor
    Mysql_link = ''
    Mysql_cusor = ''

    # 链接数据库
    def __init__(self):
        # 链接mysql
        # 打开数据库连接
        self.Mysql_link = pymysql.connect(self.Mysql_localhost,self.Mysql_username,
            self.Mysql_password,self.Mysql_select_DB,
            charset=self.Mysql_charset,cursorclass=self.Mysql_cursorclass 
            )
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.Mysql_cusor = self.Mysql_link.cursor()

    # 查询方法
    def query(self,sql):
        self.Mysql_cusor.execute(sql)
        # 返回查询结果
        return self.Mysql_cusor.fetchall()

    # 执行方法
    def exec(self,sql):
        try:
            self.Mysql_cusor.execute(sql)
            self.Mysql_link.commit()
            # 判断当前的sql是添加还是其它
            if 'insert' in sql:
                # 返回最后插入id
                userid = self.Mysql_cusor.lastrowid
                return userid
            else:
                # 返回受影响的行数
                num = self.Mysql_cusor.rowcount
                return num
          
        except:
            # 返回false
            self.Mysql_link.rollback()
            return False

    # 添加
    # def add():
    #     pass

    # 关闭数据库链接
    def __del__(self):
        self.Mysql_link.close()

# 图书
'''
id 书名 title  作者 author 封面图 价格 出版社 数量 书号  内容推荐 作者简介  目录 状态 上架日期 
'''
'''
借阅
id  bookid userid(谁借的)  时间 是否归还 0  1

'''

'''会员
id 昵称 头像 手机号  所属部门 addtime
'''




