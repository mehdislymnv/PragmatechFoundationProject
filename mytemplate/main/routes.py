from app import app
from app.models import Blog
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def site_index():
    blogs=Blog.query.all()
    return render_template('main/Blog.html',blogs=blogs)