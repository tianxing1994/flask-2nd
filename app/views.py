import math, time
from flask import Blueprint, session, render_template, request, redirect, url_for, jsonify
from app.plugin import cache
from . import models,plugin

blue = Blueprint('first',__name__)

# 配置蓝图
def blue_init(app):
    app.register_blueprint(blueprint=blue)
    plugin.plugin_init(app)


@blue.route('/test/')
def test():
    return "success!"

@blue.route('/setsess/')
def setsess():
    session['key'] = 'value'
    return 'set session success!'

@blue.route('/getsess/')
def getsess():
    result = session.get('key','not find')
    return 'the session value of key is %s' % result

# 随机增加 user 对象
@blue.route('/randomAddUser/')
def randomAddUser():
    import random
    randNum = random.randint(100,999)

    user = models.User()
    user.username = str(randNum) + 'jackMa'
    user.password = '123456'
    user.age = random.randint(16,32)
    user.sex = random.sample((True,False),1)[0]
    user.job = 'CEO of alibaba'

    models.db.session.add(user)
    models.db.session.commit()
    return 'success!'

# 客户端 form 表单增加对象
@blue.route('/addUser/', methods=['POST'])
def addUser():
    username = request.form.get("username")
    password = request.form.get("password")
    age = request.form.get("age")
    sex = request.form.get("sex")
    job = request.form.get("job")

    user = models.User()
    user.username = username
    user.password = password
    user.age = int(age)
    if sex == 'True':
        user.sex = 1
    else:
        user.sex = 0
    user.job = job

    models.db.session.add(user)
    models.db.session.commit()
    return redirect(url_for('first.queryUser'))


# 查询全部
@blue.route('/queryUser/')
def queryUser():

    users = models.User.query.all()
    print(len(users))
    # users = [models.user.query.get(4),]
    # users = models.user.query.filter(models.user.age == 24)
    # users = models.user.query.filter(models.user.age == 24).order_by(-models.user.id)
    # users = models.user.query.filter(models.user.age < 24).order_by(-models.user.age)
    # users = models.user.query.filter(models.user.age < 27).order_by(-models.user.age).limit(2)
    # users = models.user.query.filter().order_by(-models.user.age)
    # users = models.user.query.filter().order_by(-models.user.age).limit(2)
    # users = models.user.query.filter(models.user.age == 24).offset(1)
    # users = models.user.query.filter(models.user.age == 24).offset(1).limit(2)
    # users = models.user.query.filter(models.user.age == 24).limit(2).offset(1)
    # limit 始终是最后执行

    # 包含
    #users = models.user.query.filter(models.user.id.in_([1,5,6,8,12,15,20,21,25]))

    # 模糊查询
    # users = models.user.query.filter(models.user.username.startswith('2'))
    # users = models.User.query.filter(models.User.username.like('%3%'))
    return render_template("user/user.html",users=users)

# 查询分页，一页6个
@blue.route('/queryUserByPage/<int:pageNum>/')
@cache.cached(timeout=50)
def queryUserByPage(pageNum):
    all_user = models.User.query.all()
    total_pages = range(1,math.ceil(len(all_user)/6)+1)
    start = 6 * (pageNum - 1)
    end = start + 6
    users = all_user[start:end]

    return render_template("user/user.html",users=users,totalPages=total_pages)

# 根据 ID 删除
@blue.route('/deleteUser/<int:userId>')
def deleteUser(userId):
    # 删除
    try:
        users = [models.User.query.get(userId), ]
        models.db.session.delete(users[0])
        models.db.session.commit()
    except:
        pass

    return redirect(url_for('first.queryUser'))

# 批量删除
@blue.route('/deleteUser/')
def bulkDeleteUser():

    # 批量删除 - 渲染模板时 users 获取不到。
    users = models.User.query.filter(models.User.age < 20)
    for user in users:
        models.db.session.delete(user)
    models.db.session.commit()

    return render_template("user.html")


@blue.route('/editUser/<int:userId>',methods=['POST'])
def editUser(userId):
    user = models.User.query.get(userId)
    username = request.form.get("username")
    password = request.form.get("password")
    age = request.form.get("age")
    sex = request.form.get("sex")
    job = request.form.get("job")

    user.username = username
    user.password = password
    user.age = int(age)
    if sex == 'True':
        user.sex = 1
    else:
        user.sex = 0
    user.job = job

    models.db.session.add(user)
    models.db.session.commit()

    return redirect(url_for('first.queryUser'))

# 勾子函数，类似于中间件
@blue.before_request
def beforerequest():
    print("this requester id is: {}".format(request.remote_addr))


# jsonify 方法
@blue.route('/jsonify/')
def jsonifyTest():
    data = {
        "id":1,
        "name":"data",
        "age":24
    }

    response = {
        'status': 200,  # 状态码
        'time':time.time(), # 请求时间
        'message':"Success!",   # 提示信息
        'data':[data,],
    }
    return jsonify(response)
    # return str(response)










