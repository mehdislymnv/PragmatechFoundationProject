from app import app
from app.models import Blog,Leader,footer
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def site_index():
    footers=footer.query.all()
    return render_template('main/index.html',footers=footers)
   


@app.route("/blog")
def site_blog():
    blogs=Blog.query.all()
    footers=footer.query.all()
    return render_template('main/Blog.html',blogs=blogs , footers=footers)


@app.route("/leader")
def site_leader():
    leaders=Leader.query.all()
    footers=footer.query.all()
    return render_template('main/leader.html',leaders=leaders , footers=footers)

