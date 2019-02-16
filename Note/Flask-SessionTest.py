from flask import Flask, session, request
from flask_session import Session

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'redis'
app.config['PERMANENT_SESSION_LIFETIME'] = 3
app.config.from_object(__name__)
Session(app)

# 1. 用 A 浏览器访问链接以设置 session 并在页面显示 sessionid
@app.route('/setsession/<value>/')
def setsession(value):
    # print(session.sid)
    session['key'] = value
    result = session.sid
    return result

# 2. 用 A 浏览器访问链接获取 value
@app.route('/getsessionina/')
def getsessionina():
    print(request.cookies.get("session"))
    result = session.get('key', 'not set')
    return result

# 3. 用 B 浏览器访问链接，传入在 A 浏览器访问后得到的 sessionid 作为参数
@app.route('/getsessioninb/<sid>/')
def getsessioninb(sid):
    session.sid = sid
    result = session.get('key', 'not set')
    return result




if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=8000, host='0.0.0.0')
