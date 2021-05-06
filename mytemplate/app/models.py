from app import db
class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    b_title=db.Column(db.String(50))
    b_header=db.Column(db.String(50))
    b_url=db.Column(db.String(100))
    b_foto=db.Column(db.String(100))
    b_gun=db.Column(db.String(50))
    b_ay=db.Column(db.String(50))

 