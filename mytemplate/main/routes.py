from app import app
from app.models import Blog,Leader, Projects,footer
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def site_index():
   
    project=Projects.query.all()
    footers=footer.query.all()
    return render_template('main/index.html',footers=footers, project=project)
   


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

@app.route("/contacts")
def site_contact():
    footers=footer.query.all()
    return render_template('main/Contacts.html',footers=footers)


@app.route("/about")
def site_about():
    footers=footer.query.all()
    return render_template('main/about.html',footers=footers)

@app.route("/projects")
def site_projects():
    project=Projects.query.all()
    footers=footer.query.all()
    return render_template('main/Projects.html',project=project,footers=footers)