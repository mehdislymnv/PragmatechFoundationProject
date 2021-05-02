from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    f_name=db.Column(db.String(50))
    l_name=db.Column(db.String(50))
    username=db.Column(db.String(50))
    email=db.Column(db.String(50))
    Address=db.Column(db.String(50))
    Address2=db.Column(db.String(50))

@app.route("/", methods=['GET','POST'])
def add():
    if request.method=='POST':
        user=User(
            f_name=request.form['f_name'],
            l_name=request.form['l_name'],
            username=request.form['username'],
            email=request.form['email'],
            Adress=request.form['Address'],
            Address2=request.form['Address2']

        )
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    
    return render_template('index.html')
    

if __name__=='__main__':
    app.run(debug=True)
  











