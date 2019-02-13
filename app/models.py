from .plugin import db



class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyName = db.Column(db.String(20))
    companyType = db.Column(db.String(20))
    users = db.relationship('User',backref='company', lazy=True)

class User(db.Model):
    # 需要自行创建主键
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(20))
    age = db.Column(db.Integer)
    sex = db.Column(db.Boolean)
    job = db.Column(db.String(100))
    company_id = db.Column(db.Integer,db.ForeignKey(Company.id),nullable=True)
    token = db.Column(db.String(200),nullable=True)
    is_delete = db.Column(db.Boolean,default=False)

class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    phone = db.Column(db.String(20),unique=True,nullable=True)
    token = db.Column(db.String(200),nullable=True)
    is_active = db.Column(db.Boolean,default=False,nullable=False)
    is_delete = db.Column(db.Boolean,default=False,nullable=False)
