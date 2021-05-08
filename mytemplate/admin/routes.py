from app import app
from app import db
from app.models import Blog,Leader
from flask import Flask,redirect,url_for,render_template,request
import os



@app.route("/admin/")
def admin_index():
    return render_template('admin/index.html')
    
# blog router
@app.route("/admin/blog",methods=['GET','POST'])
def admin_blog():

    blogs=Blog.query.all()
    if request.method=='POST':
        file=request.files['b_foto']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        blog=Blog(
            b_title=request.form['b_title'],
            b_header=request.form['b_header'],
            b_url=request.form['b_url'],
            b_gun=request.form['b_gun'],
            b_ay=request.form['b_ay'],
            b_foto=filename


        )
        db.session.add(blog)
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('/admin/a_blog.html',blogs=blogs)

@app.route('/delete/<id>')
def delete(id):
    blogs=Blog.query.get(id)
    db.session.delete(blogs)
    db.session.commit()
    return redirect('/admin/blog')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    bl=Blog.query.get(id)
    if request.method=='POST':
        bl.b_title=request.form['b_title']
        bl.b_header=request.form['b_header']
        bl.b_url=request.form['b_url']
        bl.b_gun=request.form['b_gun']
        db.session.commit()
        return redirect('/admin')
    
    return render_template('admin/update.html',bl=bl)

# leader router
@app.route("/admin/leader",methods=['GET','POST'])
def admin_leader():

    leaders=Leader.query.all()
    if request.method=='POST':
        file=request.files['l_foto']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        leader=Leader(
            l_name=request.form['l_name'],
            l_header=request.form['l_header'],
            l_position=request.form['l_position'],
            f_url=request.form['f_url'],
            t_url=request.form['t_url'],
            g_url=request.form['g_url'],
            l_foto=filename


        )
        db.session.add(leader)
        db.session.commit()
        return redirect('/admin/leader')
    return render_template('/admin/l.html',leaders=leaders)
