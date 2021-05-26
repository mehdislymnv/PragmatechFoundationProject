# auth routes

from app import app
from app import db
import os
from flask import render_template,redirect,request,url_for,make_response

loginData={
    'username' : 'admin',
    'password' : 'admin'
}

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']==loginData['username'] and request.form['password']==loginData['password']:
            resp = make_response(redirect(url_for('admin_index')))
            resp.set_cookie('loginStatus', 'beli')
            return resp    
        else:
            return render_template('auth/login.html')
    return render_template('auth/login.html')