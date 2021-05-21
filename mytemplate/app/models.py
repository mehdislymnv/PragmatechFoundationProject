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
    f_location=db.Column(db.String(50))
    f_email=db.Column(db.String(50))
    f_number=db.Column(db.String(50))
    f_facebook=db.Column(db.String(100))
    f_twitter=db.Column(db.String(100))
    f_youtube=db.Column(db.String(100))
    f_insdagram=db.Column(db.String(100))


class Projects(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    p_title=db.Column(db.String(50))
    p_header=db.Column(db.String(50))
    p_url=db.Column(db.String(100))
    p_foto=db.Column(db.String(100))


class about(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    a_title=db.Column(db.String(50))
    a_header=db.Column(db.String(50))
    a_url=db.Column(db.String(100))
    a_foto=db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(50))
   