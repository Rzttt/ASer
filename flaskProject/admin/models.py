from sqlalchemy import true
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

class user(UserMixin,db.Model):
    __tablename__ = 'admin'
    __table_args__ = {'extend_existing': True}
    username = db.Column('name',db.String(20))
    password_hash = db.Column('password',db.String(128))
    Authority = db.Column('Authority',db.Integer,default=3)
    id = db.Column('id',db.Integer,primary_key=true,unique=true)

    def get_user(self):
        return {
            'name':self.username,
            'password':self.password_hash,
            'Authority':self.Authority
        }

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class db_deal:
    def get_user(self):
        u = db.session.query(user).first()
        return u
@login.user_loader
def load_user(id):
    return user.query.get(int(id))