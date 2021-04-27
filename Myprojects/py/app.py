from typing import ClassVar
from flask import Flask,render_template,request,redirect


app=Flask(__name__)
students=[]
class Student():
    def __init__(self,_name,_surname,_seher,_email):
        self.ad=_name
        self.soyad=_surname
        self.seher=_seher
        self.email=_email


indexData='index page data'
aboutData={
    'title':'About Page',
    'content':'Lorem ipsum dolor sit amet',
}
contactData='contact page data'
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        _ad=request.form['ad']
        _soyad=request.form['soyad']
        _seher=request.form['seher']
        _email=request.form['email']
        user=Student(_ad,_soyad,_seher,_email)
        students.append(user)
        return redirect('/about')
    return render_template('index.html',stud=students)
    

@app.route('/about')
def about():
   return render_template('about.html',stud=students)

@app.route('/contact')
def contact():
    return contactData

if __name__=='__main__':
    app.run(debug=True)