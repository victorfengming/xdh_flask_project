'''
# 导包
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

'''
import pymysql

# 把pymysql的操作给他封装到一个类里面
class Model():
    # 属性
    Mysql_localhost = '127.0.0.1'
    Mysql_username = 'root'
    Mysql_password = ''
    Mysql_select_DB = 'wxapp'
    Mysql_charset = 'utf8mb4'
    Mysql_cursorclass = pymysql.cursors.DictCursor
    Mysql_link = ''
    Mysql_cursor = ''

    def __init__(self):
        # 连接数据库
        self.Mysql_link = pymysql.connect(
            self.Mysql_localhost,
            self.Mysql_username,
            self.Mysql_password,
            self.Mysql_select_DB,
            charset = self.Mysql_charset,
            cursorclass=self.Mysql_cursorclass
        )
        self.Mysql_cursor = self.Mysql_link.cursor()


    # 查询方法
    def query(self,sql):
        self.Mysql_cursor.execute(sql)
        # 返回 查询结果
        return self.Mysql_cursor.fetchall()
        pass

    # 执行方法
    def exec(self,sql):
        try:
            self.Mysql_cursor.execute(sql)
            self.Mysql_link.commit()
            # fanhui
            num = self.Mysql_cursor.rowcount
            return num
        except:
            self.Mysql_link.rollback()
            return False
        pass

    # 关闭数据库连接
    def __del__(self):
        self.Mysql_link.close()


# 图书
'''
表中有哪些字段
id  
书名 title
作者 author
封面图
价格 
出版社
数量
书号
内容推荐 
作者简介
目录
状态
上架日期
'''
# 豆瓣 有个api接口,只要你提供书号,就能返回所有相关信息

'''
借阅
id
bookid
谁接的
时间
借阅时长
预计归还时间
是否归还 0 1
'''

'''
会员表
    id
    昵称
    手机号
    openid
        (这个不是用户原始的id),
        这个能够判断你关没关注这个公众号
    所属部门
    token
        这个可NB了,
        我获取用户信息后,我怎么知道登录没呢
        这回可没有session,所有要整个介玩意
'''

if __name__ == '__main__':

    # # method1
    # m = Model()
    # res = m.query('select * from user')
    # print(res)


    # # method2
    # res = Model().query('select * from user')

    # # method3
    res = Model().exec('insert into user(name) values("wakdwl"),("iuru"),("guakqu")')
    print(res)