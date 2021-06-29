from flask import Flask
from flask import request
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/login', methods=['POST', 'GET'])
@app.route('/login/<name>')
def login(name=None):
    return render_template('login.html', name=name)