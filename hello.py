from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=8000, host='0.0.0.0')

# 执行本文件， 后访问 http://127.0.0.1:5000/ 可看到 Hello World! 在浏览器页面