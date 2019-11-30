微信小程序+flask 项目设计
图书借阅小程序
    图书列表
    图书详情
    图书查询
    图书录入
    图书借阅,归还
    个人中心,借阅信息

flask
    api 小程序api接口服务
    admin    后台管理
        图书管理
            添加
            查询
            修改
            下架
        借阅管理
            查看
            修改
        用户管理
            查看所有注册使用的用户,修改状态
        
        
查询到的数据json格式不能直接转换成为可用的类型

这可咋整        

我们需要处理一下才能转出去

# pymysql复习
1. 连接mysql数据库
2. 创建游标对象
3. 执行sql语句
4. 返回结果
5. 关闭连接

```python

# 导包
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()
```


其中书籍的信息可以通过书号拿到

我们先写一个,表单的

内容可以参考:https://book.douban.com/