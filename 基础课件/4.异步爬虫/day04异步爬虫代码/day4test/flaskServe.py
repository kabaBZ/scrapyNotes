from flask import Flask, render_template
from time import sleep

app = Flask(__name__)


@app.route('/kaba')
def index_1():
    sleep(2)
    return render_template('test.html')


@app.route('/jay')
def index_2():
    sleep(2)
    return render_template('test.html')


@app.route('/tom')
def index_3():
    sleep(2)
    return render_template('test.html')


if __name__ == "__main__":
    # debug=True表示开启调试模式：服务器端代码被修改后按下保存键会自动重启服务
    app.run(debug=True)
