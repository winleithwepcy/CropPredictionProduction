from datetime import datetime
from crop import db

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(20), unique=True, nullable=False)
    condition = db.Column(db.String(120), unique=True, nullable=False)   

    def __repr__(self):
        return f"Crop('{self.location}', '{self.condition}')"

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"News('{self.title}', '{self.date_posted}')"

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Article('{self.title}', '{self.date_posted}')"   

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    soiltype = db.Column(db.String(100), nullable=False)
    croptype = db.Column(db.String(100), nullable=False)
    seedquality = db.Column(db.String(100), nullable=False)
    seedrate = db.Column(db.Integer, nullable=False)
    fertilizertype = db.Column(db.String(100), nullable=False)
    manuretype = db.Column(db.String(100), nullable=False)
    landpreparation = db.Column(db.String(100), nullable=False)
    sowingtype = db.Column(db.String(100), nullable=False)
    fertilizeramt = db.Column(db.Integer, nullable=False)
    herbicideamt= db.Column(db.Integer, nullable=False)
    insecticideamt = db.Column(db.Integer, nullable=False)
    manureamt = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Survey('{self.croptype}', '{self.soiltype}')"              