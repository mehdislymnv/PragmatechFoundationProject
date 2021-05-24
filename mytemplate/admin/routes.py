from app import app
from app import db
from app.models import Blog,Leader,footer,Projects,about,User,Contacts
from flask import Flask,redirect,url_for,render_template,request,session,make_response
import os

from enum import unique




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
def delete_blog(id):
    blogs=Blog.query.get(id)
    db.session.delete(blogs)
    db.session.commit()
    return redirect('/admin/blog')

@app.route('/update/<id>',methods=['GET','POST'])
def update_blog(id):
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

        lead=Leader(
            l_name=request.form['l_name'],
            l_header=request.form['l_header'],
            l_position=request.form['l_position'],
            f_url=request.form['f_url'],
            t_url=request.form['t_url'],
            g_url=request.form['g_url'],
            l_foto=filename


        )
        db.session.add(lead)
        db.session.commit()
        return redirect('/admin/leader')
    return render_template('/admin/l.html',leaders=leaders)

# leader CRUD


@app.route('/delete_l/<id>')
def delete_leader(id):
    
    leaders=Leader.query.get(id)
    db.session.delete(leaders)
    db.session.commit()
    return redirect('/admin/leader')

@app.route('/update_l/<id>',methods=['GET','POST'])
def update_leader(id):
    lea=Leader.query.get(id)
    if request.method=='POST':
        lea.l_name=request.form['l_name']
        lea.l_header=request.form['l_header']
        lea.l_position=request.form['l_position']
        lea.f_url=request.form['f_url']
        lea.t_url=request.form['t_url']
        lea.g_url=request.form['g_url']
        db.session.commit()
        return redirect('/admin')
    
    return render_template('admin/update_l.html',lea=lea)




#foorer router
@app.route("/admin/footer",methods=['GET','POST'])
def admin_footer():
    
    footers=footer.query.all()
    if request.method=='POST':
        ft=footer(
            f_location=request.form['f_location'],
            f_email=request.form['f_email'],
            f_number=request.form['f_number'],
            f_facebook=request.form['f_facebook'],
            f_twitter=request.form['f_twitter'],
            f_youtube=request.form['f_youtube'],
            f_insdagram=request.form['f_insdagram']
        )
        db.session.add(ft)
        db.session.commit()
        return redirect('/admin/footer')
    return render_template('/admin/footer.html',footers=footers) 


#footer CRUD
@app.route('/delete_f/<id>')
def delete_footer(id):
    
    footers=footer.query.get(id)
    db.session.delete(footers)
    db.session.commit()
    return redirect('/admin/footer')

@app.route('/update_f/<id>',methods=['GET','POST'])
def update_footer(id):
    fto=footer.query.get(id)
    if request.method=='POST':
        fto.f_location=request.form['f_location']
        fto.f_email=request.form['f_email']
        fto.f_number=request.form['f_number']
        fto.f_facebook=request.form['f_facebook']
        fto.f_twitter=request.form['f_twitter']
        fto.f_youtube=request.form['f_youtube']
        fto.f_insdagram=request.form['f_insdagram']
        db.session.commit()
        return redirect('/admin')
    
    return render_template('admin/update_f.html',fto=fto)

#Projects router

@app.route("/admin/projects",methods=['GET','POST'])
def admin_Projects():
    project=Projects.query.all()
    if request.method =='POST':
        file=request.files['p_foto']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        proje=Projects(
            p_title=request.form['p_title'],
            p_header=request.form['p_header'],
            p_url=request.form['p_url'],
            p_foto=filename
        )
        db.session.add(proje)
        db.session.commit()
        return redirect('/admin/projects')
    return render_template('/admin/a_Projects.html',project=project)
#Projects CRUD
@app.route('/delete_p/<id>')
def delete_projects(id):
    
    project=Projects.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect('/admin/projects')


@app.route('/update_p/<id>',methods=['GET','POST'])
def update_project(id):
    Pro=Projects.query.get(id)
    if request.method=='POST':
        Pro.p_title=request.form['p_title']
        Pro.p_header=request.form['p_header']
        Pro.p_url=request.form['p_url']
        db.session.commit()
        return redirect('/admin')
    
    return render_template('/admin/update_p.html',Pro=Pro)


@app.route("/admin/abou",methods=['GET','POST'])
def admin_abou():
    abouts=about.query.all()
    if request.method =='POST':
        file=request.files['a_foto']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        ab=about(
            a_title=request.form['a_title'],
            a_header=request.form['a_header'],
            a_url=request.form['a_url'],
            a_foto=filename
        )
        db.session.add(ab)
        db.session.commit()
        return redirect('/admin')
    return render_template('/admin/a_about.html',abouts=abouts )


@app.route("/admin/login",methods=['GET','POST'])
def admin_login():
    users=User.query.all()
    if request.method=='POST':
        for user in users:
            if user.username==request.form['username']:
                if user.password==request.form['password']: 
                    resp = make_response(render_template('profile.html',user=user))
                    resp.set_cookie('loginStatus', str(user.id))
                    return resp
                   
                else:
                    return redirect('/login')

    
    return render_template('/admin/login.html')
    


@app.route("/index/contact",methods=['GET','POST'])
def admin_abou():
    abouts=Contacts.query.all()
    if request.method =='POST':
        
        ab=Contacts(
            C_username=request.form['C_username'],
            C_email=request.form['C_email'],
            C_wepsite=request.form['C_wepsite'],
            C_company=request.form['C_company']
           
        )
        db.session.add(ab)
        db.session.commit()
        return redirect('/contacts')
    return render_template('main/Blog.html')