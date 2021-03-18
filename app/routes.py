from app import app
from flask import render_template


@app.route('/')    # cria uma rota default
@app.route('/index')
def index():
    user = {'username' : 'Pedro'}
    title = "Homepage"
    posts = [
        {'author': {'username': 'Maria'}, 'body': "Olá da Maria"},
        {'author': {'username': 'Pedro'}, 'body': "Olá!"}
    ]
    return render_template("index.html", user=user, posts=posts, title=title)   # renderiza um arquivo html


