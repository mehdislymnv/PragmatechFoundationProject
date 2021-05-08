from app import app
from app.models import Blog,Leader
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def site_index():
    
    return render_template('main/index.html')


@app.route("/blog")
def site_blog():
    blogs=Blog.query.all()
    return render_template('main/Blog.html',blogs=blogs)


@app.route("/leader")
def site_leader():
    leaders=Leader.query.all()
    return render_template('main/leader.html',leaders=leaders)