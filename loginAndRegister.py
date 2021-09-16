from operator import is_not
from flask import Flask
from flask import make_response
from flask import request
from flask_script import Manager
import os
import json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'userConfigBase.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
userdb=SQLAlchemy(app)
manager=Manager(app)
@app.route('/')
def test():
    return '服务器正常运行'

class userInfoTable(userdb.Model):
    __tablename__='userInfo'
    id=userdb.Column(userdb.Integer,primary_key=True)
    username=userdb.Column(userdb.String,unique=True)
    password=userdb.Column(userdb.String)

    def __repr__(self):
        return 'table name is '+self.username

#此方法处理用户登录 返回码为0无注册 返回码为1密码错误
@app.route('/user',methods=['POST'])
def check_user():
    # 处理json数据
    data = json.loads(request.data) #将json字符串转换为dict
    haveregisted = userInfoTable.query.filter_by(username = data['username']).all()
    if haveregisted.__len__() is not 0: # 判断是否已被注册
        passwordRight = userInfoTable.query.filter_by(username = data['username'],password = data['password']).all()
        if passwordRight.__len__() is not 0:
            return '登录成功'
        else:
            return '1'
    else:
        return '0'


#此方法处理用户注册
@app.route('/register',methods=['POST'])
def register():
    # 处理json数据
    data = json.loads(request.data) #将json字符串转换为dict
    userdb.create_all()
    haveregisted = userInfoTable.query.filter_by(username = data['username']).all()
    if haveregisted.__len__() is not 0: # 判断是否已被注册
        return '0'
    userInfo=userInfoTable(username = data['username'], password = data['password'])
    userdb.session.add(userInfo)
    userdb.session.commit()
    return '注册成功'

if __name__ == '__main__':
    manager.run()
