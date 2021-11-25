from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateTimeField, DateField, \
    TimeField, FileField

from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField('name',validators=[DataRequired()],render_kw={"placeholder": "用户名"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "密码"})
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('登录',render_kw={"class":"btn btn-success"})


class db_add(FlaskForm):
    name = StringField('name',validators=[DataRequired()],render_kw={"placeholder":'名字','class':"span11"})
    email = StringField('email',validators=[DataRequired(),Email()],
                        render_kw={"placeholder": "邮箱",'class':"span11"})
    message = TextAreaField('message',validators=[DataRequired()], render_kw={'class':"span11"})
    content = TextAreaField('content',validators=[DataRequired()], render_kw={'class':"span11",'cols':'30' ,'rows':'10'})
    introduction = TextAreaField('introduction',validators=[DataRequired()], render_kw={'class': "span11"})
    location = StringField('location',validators=[DataRequired()], render_kw={'class':"span11"})
    time = DateTimeField('time',validators=[DataRequired()], default=datetime.now,render_kw={'class':"span11"})
    date = DateField('date',validators=[DataRequired()], render_kw={'class':"span11"})
    t = TimeField('t',validators=[DataRequired()], render_kw={'class':"span11"})
    img_path = FileField('img_path',validators=[DataRequired()], render_kw={'class':"span11"})
    img_path_small = FileField('img_path_small',validators=[DataRequired()], render_kw={'class':"span11"})


    id = StringField('id',validators=[DataRequired()], render_kw={'class':"span11"})
    type = StringField('type',validators=[DataRequired()], render_kw={'class':"span11"})
    avatar = FileField('avatar',validators=[DataRequired()], render_kw={'class':"span11"})
    department = StringField('department',validators=[DataRequired()], render_kw={'class':"span11"})
    sub = SubmitField('提交',render_kw={'class':"btn btn-success"})
    def get_content(self):
        return {
            'name':self.name.data,
            'email':self.email.data,
            'message':self.message.data,
            'time':self.time.data,
            'date':self.date.data,
            't':self.t.data,
            'img_path':self.img_path.data,
            'img_path_small':self.img_path_small.data,
            'introduction':self.introduction.data,
            'content':self.content.data,
            'id':self.id.data,
            'type':self.type.data,
            'avatar':self.avatar.data,
            'department':self.department.data,
            'location':self.location.data,
        }