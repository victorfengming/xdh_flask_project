from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/myapp"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 绑定app至SQLAlchemy
db = SQLAlchemy(app)



#会员模型
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd= db.Column(db.String(100))
    email= db.Column(db.String(100))
    phone= db.Column(db.String(11))
    info= db.Column(db.Text)
    face = db.Column(db.String(255))
    addtime = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.name

class Stu(db.Model):
    __tablename__ = 'Stu'

    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(10))
    email = db.Column(db.String(50))
    age = db.Column(db.Integer)


if __name__ == "__main__":

    # # 创建数据表
    # db.create_all()

    # # 查询数据
    # res = User.query.all()
    # print(res)
    # print('-'*80)
    # print(dir(res[0]))
    # print('-'*80)
    # # print(type(res[0]).__dict__)
    #
    # # 数据的添加
    # # 先创建一个模型对象
    # s = Stu()
    # s.sname = '战三'
    # s.email = 'zssag@163.com'
    # s.age = 18
    # # db 是之前的实例化的对象
    # # 这里的session不是session仅仅表示会话的意思
    # db.session.add(s)
    # # 你要知道,这不是一个人开发的啊
    # # 那你学django的时候是那样用的,这回这样用,
    # # 那就这样了,用人家的东西就得挺着
    # # 那要完全都一样全写一个样,就用一个框架不就oK了么
    # # 这个要求是SQLAlchemy要求的,
    # # 这个时候还可以捕获异常,db.rollback还可以回滚,也就是说自带了事务处理了
    # db.session.commit()
    #
    # # 数据添加2.
    # # 这个数据实际上应该从表单中添加过来的,
    # data = {'sname':'lisi','email':'lsasdfghafsgh@qq.com','age':21}
    # # **拆参数,这个经常用,得理解
    # s = Stu(**data)
    # db.session.add(s)
    # db.session.commit()

    #
    # # 删除
    # # 先获取对象
    # ob = Stu.query.get(2)
    # db.session.delete(ob)
    # db.session.commit()
    #
    # # 修改
    # ob = Stu.query.get(1)
    # ob.sname = '张三'
    # db.session.add(ob)
    # db.session.commit()


    # 查询
    # all()获取所有 get() 获取一个指定对象
    pass


