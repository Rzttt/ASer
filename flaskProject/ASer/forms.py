from flask_wtf import FlaskForm
from wtforms import StringField,  TextAreaField
from wtforms.validators import DataRequired, Email


class feedback(FlaskForm):
        name = StringField('name',validators=[DataRequired()],render_kw={"placeholder": "姓名"})
        email = StringField('email',validators=[DataRequired(),Email()],
                            render_kw={"placeholder": "邮箱"})
        message = TextAreaField('message',validators=[DataRequired()],render_kw={'cols':'30' ,'rows':'10'})

        def send(self):
            dic = {'email':self.email.data,'name':self.name.data,'message':self.message.data}

            return dic

class Comment(FlaskForm):
    name = StringField('name',validators=[DataRequired()],render_kw={"placeholder": "name"})
    email = StringField('email', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Email"})
    message = TextAreaField('message', validators=[DataRequired()], render_kw={'cols': '30', 'rows': '10'})

    def get_comment(self):
        dic = {'email': self.email.data, 'name': self.name.data, 'message': self.message.data}

        return dic