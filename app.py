from flask import Flask, render_template

app = Flask(__name__)


@app.route('/abc')
def abc():
    return 'abc World!'


@app.route('/')
def index():
    return render_template('index.html',username='mengya')


@app.route('/love')
def love():
    return '<h1 style="color:red;">abc World!</h1>'


if __name__ == '__main__':
    app.run()


