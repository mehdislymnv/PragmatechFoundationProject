from app import db
class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    b_title=db.Column(db.String(50))
    b_header=db.Column(db.String(50))
    b_url=db.Column(db.String(100))
    b_foto=db.Column(db.String(100))
    b_gun=db.Column(db.String(50))
    b_ay=db.Column(db.String(50))

 
class Leader(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    l_name=db.Column(db.String(50))
    l_position=db.Column(db.String(50))
    l_header=db.Column(db.String(50))
    l_foto=db.Column(db.String(100))
    f_url=db.Column(db.String(100))
    t_url=db.Column(db.String(100))
    g_url=db.Column(db.String(100))

 

class footer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    location=db.Column(db.String(50))
    email=db.Column(db.String(50))
    number=db.Column(db.String(50))
    facebook=db.Column(db.String(100))
    twitter=db.Column(db.String(100))
    youtube=db.Column(db.String(100))
    insdagram=db.Column(db.String(100))