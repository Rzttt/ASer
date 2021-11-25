import os
import random
from flask import Flask, Blueprint, render_template, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, AUDIO,configure_uploads
from sqlalchemy import true

from ASer.forms import feedback
from ASer.send_email import ASer_email

from flask_login import login_required, LoginManager
from config import ASer_db
app = Flask(__name__)
app.config.from_object(ASer_db)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
email_ = ASer_email()
file = UploadSet('MYFILE')
app.config['UPLOADED_MYFILE_DEST'] = os.path.join(os.path.dirname(__file__),'static','images')

configure_uploads(app,file)
month_list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def month_change(month):
    return month_list[month-1]
def get_introduction(content):
    if len(content) > 60:
        return content[0:60]+'...'
    else:
        con = content+'....'
        return con


class member(db.Model):
    __tablename__ ='minister'
    __table_args__ = {'extend_existing': True}
    id=db.Column('id',db.Integer)
    name = db.Column('name',db.String(20),primary_key=True,unique=True)
    img_path = db.Column('img_path',db.String(50))
    department = db.Column('department',db.String(10))
    introduction = db.Column('introduction',db.String(600))
    def get_member(self):
        return {
            'name':self.name,
            'img_path':self.img_path,
            'department':self.department,
            'introduction':self.introduction,
            'id':self.id
        }
    def get_attributes(self):
        return ['id','name','img_path','department','introduction']
class suggestion(db.Model):
    __tablename__ = 'suggestion'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name',db.String(10))
    email = db.Column('email',db.String(30))
    message = db.Column('message',db.String(600))
    id = db.Column('index',db.Integer,primary_key=True)
    def get_suggestion(self):
        return {
            'name': self.name,
            'email': self.email,
            'message':self.message,
            'id':self.id
        }
    def get_attributes(self):
        return ['name','email','message','id']
class activity(db.Model):
    __tablename__ = 'activity'
    __table_args__ = {'extend_existing': True}
    activity = db.Column('name',db.String(30),primary_key=True)
    time = db.Column('time',db.DateTime)
    def get_activity(self):
        return {
            'activity':self.activity,
            'time':self.time,
            'year':self.time.year,
            'month':self.time.month,
            'day':self.time.day,
            'tim':str(str(self.time.hour)+':'+str(self.time.minute))
        }

    def get_attributes(self):
        return ['activity','time']
class event(db.Model):
    __tablename__='events'
    __table_args__ = {'extend_existing': True}
    event = db.Column('name',db.String(30),primary_key=True)
    time=db.Column('time',db.TIME)
    img_path = db.Column('img_path',db.String(50))
    date = db.Column('date',db.DATE)
    content =db.Column('content',db.String(600))
    location = db.Column('location',db.String(40))
    id = db.Column('id',db.Integer,unique=True)
    def get_event(self):
        return {
            'event':self.event,
            'time':self.time,
            'img_path':self.img_path,
            'date':self.date,
            'month':month_change(self.date.month),
            'day':self.date.day,
            'location':self.location,
            'content':self.content,
            'id':self.id,
            'introduction':get_introduction(self.content)
        }

    def get_attributes(self):
        return ['event', 'time', 'img_path', 'date', 'content', 'location','id',]

class comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name',db.String(30))
    email = db.Column('email',db.String(50))
    id = db.Column('id',db.Integer)
    index_ = db.Column('index_',db.Integer,primary_key=True)
    message = db.Column('message',db.String(600))
    avatar = db.Column('avatar',db.String(50))
    type_c = db.Column('type',db.Integer)
    def get_comment(self):
        return {
            'name':self.name,
            'email':self.email,
            'id':self.id,
            'index':self.index_,
            'message':self.message,
            'avatar':self.avatar,
            'type':self.type_c

        }

    def get_attributes(self):
        return ['name', 'email', 'id', 'index','message', 'avatar','type']
class news(db.Model):
    __tablename__='anime_news'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name',db.String(50))
    index=db.Column('index',db.Integer,unique=True,primary_key=true)
    date = db.Column('date',db.DATE)
    time = db.Column('time',db.TIME)
    content = db.Column('content',db.TEXT)
    img_path = db.Column('img_path',db.String(60))
    img_path_small = db.Column('img_path_small',db.String(80))
    introduction = db.Column('introduction',db.String(200))
    def get_new(self):
        return {
            'name': self.name,
            'time': self.time,
            'img_path': self.img_path,
            'img_path_small': self.img_path_small,
            'date': self.date,
            'month': month_change(self.date.month),
            'day': self.date.day,
            'content': self.content,
            'id': self.index,
            'introduction': self.introduction
        }
    def get_attributes(self):
        return ['name','index','date','time','content','img_path','img_path_small','introduction']
class story(db.Model):
    __tablename__ = 'story'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name',db.String(30))
    img_path = db.Column('img_path',db.String(60))
    content = db.Column('content',db.TEXT)
    index = db.Column('index',db.Integer,primary_key=true,unique=true)
    def get_story(self):
        return {
            'name':self.name,
            'img_path':self.img_path,
            'content':self.content,
            'index':self.index
        }

    def get_attributes(self):
        return ['name','img_path','content','index']
class db_deal:
    img_path = '../static/images/avatar/{}.png'
    img_list = []


    def __init__(self):
        for i in range(1,21):
            self.img_list.append(self.img_path.format(i))


    def get_members(self):
        member_list = []
        m = db.session.query(member).order_by(member.id).all()
        for i in m:
            member_list.append(i.get_member())


        return member_list

    def get_activity(self):

        future_activity = db.session.query(activity).order_by(db.desc(activity.time)).first()

        return future_activity.get_activity()
    def get_activity_all(self):
        future_activity = db.session.query(activity).all()
        activity_list = []
        for i in future_activity:
            activity_list.append(i.get_activity())

        return activity_list
    def get_event(self):
        event_list = []
        events = db.session.query(event).all()
        for i in events:
            event_list.append(i.get_event())

        return event_list
    def get_event_by_name(self, event_name):
        event_ = db.session.query(event).filter(event.event == event_name).first()
        return event_.get_event()
    def get_comments(self,id,type_c):
        comments = []
        m = db.session.query(comment).filter(comment.id==id,comment.type_c==type_c).all()
        for i in m:
            comments.append(i.get_comment())
        return comments
    def get_comments_all(self):
        comments = []
        m = db.session.query(comment).all()
        for i in m:
            comments.append(i.get_comment())
        return comments
    def get_suggestion(self):
        suggestion_list = []
        s = db.session.query(suggestion).all()
        for i in s:
            suggestion_list.append(i.get_suggestion())

        return suggestion_list
    def get_news(self):
        news_list = []
        new = db.session.query(news).order_by(db.desc(news.date)).all()
        for i in new:
            news_list.append(i.get_new())
        return news_list
    def get_new_by_name(self,name):
        new = db.session().query(news).filter(news.name==name).first()

        return new.get_new()
    def get_stories(self):
        story_list = []
        stories = db.session().query(story).all()
        for i in stories:
            story_list.append(i.get_story())
        return story_list
    def add_member(self,name,img_path, department,introduction,id):
        db.session.add(member(name=name,img_path=img_path, department=department,introduction=introduction,id=id))
        try:
            db.session.commit()
            return 1
        except:
            db.session.rollback()
            return 0
    def add_activity(self,name,time):
        db.session.add(activity(activity=name,time=time))
        try:
            db.session.commit()
            return 1
        except:
            db.session.rollback()
            return 0
    def add_suggestion(self,infor):


        db.session.add(suggestion(name=infor['name'],email=infor['email'],message=infor['message']))
        try:
            db.session.commit()
            return 1;
        except:
            db.session.rollback()
            return 0;
    def add_comment(self,com,id,type_c):

        avatar = db.session.query(comment).filter(comment.email ==com['email']).first()

        if avatar == None:
            db.session.add(comment(name=com['name'], email=com['email'], message=com['message'],avatar=random.choice(self.img_list),id=id,type_c=type_c))
        else:
            db.session.add(comment(name=com['name'], email=com['email'], message=com['message'],
                                   avatar=avatar.get_comment()['avatar'], id=id,type_c=type_c))

        try:
            db.session.commit()
            return 1
        except:
            db.session.rollback()
            return 0
    def add_event(self,name,location,message,date,t,img_path):
        db.session.add(event(event=name,location=location,content=message,date=date,time=t,img_path=img_path))
        try:
            db.session.commit()
            return 1
        except:
            db.session.rollback()
            return 0
    def add_news(self,name,img_path,img_path_small,date,t,message,introduction):
        db.session.add(news(name=name,img_path=img_path,img_path_small=img_path_small,date=date,time=t,content=message,introduction=introduction))
        try:
            db.session.commit()
            return 1
        except:
            db.session.rollback()
            return 0
    def add_story(self,name,img_path,message):
        db.session.add(story(name=name,img_path=img_path,content=message))
        try:
            db.session.commit()
            return 1
        except:
            db.session.rollback()
            return 0
    def get_attributes(self,db_name):
        if db_name == 'member':
            return member.get_attributes(member)
        elif db_name == 'suggestion':
            return suggestion.get_attributes(suggestion)
        elif db_name == 'activity':
            return activity.get_attributes(activity)
        elif db_name == 'event':
            return event.get_attributes(event)
        elif db_name == 'comment':
            return comment.get_attributes(comment)
        elif db_name=='news':
            return news.get_attributes(news)
        elif db_name=='story':
            return story.get_attributes(story)
    def get_db_by_name(self,db_name):
        if db_name == 'member':
            return self.get_members()
        elif db_name == 'suggestion':
            return self.get_suggestion()
        elif db_name == 'activity':
            return self.get_activity_all()
        elif db_name == 'event':
            return self.get_event()
        elif db_name == 'comment':
            return self.get_comments_all()
        elif db_name=='news':
            return self.get_news()
        elif db_name=='story':
            return self.get_stories()

    def add_db_by_name(self,db_name,dic):
        if db_name == 'member':
            return self.add_member(name=dic['name'],img_path=dic['img_path'],department=dic['department'],introduction=dic['introduction'],
                                   id=int(dic['id']))
        elif db_name == 'suggestion':
            return self.add_suggestion(dic)
        elif db_name == 'activity':
            return self.add_activity(name=dic['name'],time=dic['time'])
        elif db_name == 'event':
            return self.add_event(name=dic['name'],location=dic['location'],message=dic['message'],
                                  date=dic['date'],t=dic['t'],img_path=dic['img_path'])
        elif db_name == 'comment':
            return self.add_comment(com=dic,id=int(dic['id']),type_c=int(dic['type']))
        elif db_name=='news':
            return self.add_news(name=dic['name'],img_path=dic['img_path'],img_path_small=dic['img_path_small'],
                                 date=dic['date'],t=dic['t'],message=dic['message'],introduction=dic['introduction'])
        elif db_name=='story':
            return self.add_story(name=dic['name'],img_path=dic['img_path'],message=dic['message'])
db_deal_ = db_deal()




@app.route('/staff')
def staff():
    event = db_deal_.get_activity()
    res = db_deal_.get_members()
    return render_template('staff.html',res=res,event=event)

user_bp = Blueprint('user',__name__)

from ASer import routes
login = LoginManager()
login.login_view = 'admin.login'
login.init_app(app)


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


from admin import admin
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
