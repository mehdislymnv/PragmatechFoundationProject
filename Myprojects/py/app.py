from typing import ClassVar
from flask import Flask,render_template,request,redirect

app=Flask(__name__)
kitablar=[]
id=1
class kitab():
    def __init__(self,id,ad,qiymet,yazar):
        self.id=id
        self.ad=ad
        self.qiymet=qiymet
        self.yazar=yazar
       


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        _id=request.form['id']
        _ad=request.form['ad']
        _qiymet=request.form['qiymet']
        _yazar=request.form['yazar']
       
        user=kitab(_ad,_qiymet,_yazar,_id)
        kitablar.append(user)
        return redirect('/about')
    return render_template('index.html',stud=kitablar)
    

@app.route('/about')
def about():
   return render_template('about.html',stud=kitablar)



if __name__=='__main__':
    app.run(debug=True)




























"""kitablar=[]
class kitab():
    def __init__(self,ad,qiymet,yazar):
        self.ad=ad
        self.qiymet=qiymet
        self.yazar=yazar
        
        
       

a=kitab("mehdi","sa","sadasd")
b=kitab("mdi","sa","sadasd")
c=kitab("mdi","sa","sadasd")
kitablar.append(a)
kitablar.append(b)
kitablar.append(c)



for i in kitablar:
    print(i.ad,i.qiymet,i.yazar)

class uzunluq():

    def __init__(self,deyer):
        self.deyer=deyer
        print(len(self.deyer))

p1=uzunluq("mehdi")
"""


"""
"""