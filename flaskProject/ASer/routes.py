from flask import render_template, url_for
from flask import redirect

from ASer.forms import feedback,Comment
from app import app, email_, db_deal_


@app.route('/contacts',methods=['post','get'])
def contact():
    event = db_deal_.get_activity()
    feed = feedback()
    if  feed.validate_on_submit():
        infor = feed.send()
        db_deal_.add_suggestion(infor=infor)
        email_.send_email(infor)
        return redirect(url_for('contact'))

    return render_template('contacts.html',form=feed,event=event)

@app.route('/home',methods=['post','get'])
def home():
    event = db_deal_.get_activity()
    activity = db_deal_.get_event()
    news = db_deal_.get_news()
    feed = feedback()
    if feed.validate_on_submit():
        infor = feed.send()
        db_deal_.add_suggestion(infor=infor)
        email_.send_email(infor)
    return  render_template('home.html',event=event,activity=activity,news=news,form=feed)
@app.route('/',methods=['post','get'])
def index():

    event = db_deal_.get_activity()
    activity = db_deal_.get_event()

    news = db_deal_.get_news()
    feed = feedback()
    if feed.validate_on_submit():
        infor = feed.send()
        db_deal_.add_suggestion(infor=infor)
        email_.send_email(infor)
    return render_template('home.html', event=event, activity=activity,news=news,form=feed)
@app.route('/typography')
def typography():
    event = db_deal_.get_activity()

    return render_template('typography.html',event=event)

@app.route('/event/<event_name>',methods=['post','get'])
def event_detail(event_name):
    print(event_name)
    event = db_deal_.get_activity()
    activity = db_deal_.get_event_by_name(event_name)
    type = 1
    comments = db_deal_.get_comments(id=activity['id'],type_c=type)
    comment = Comment()
    if comment.validate_on_submit():
        com = comment.get_comment()

        db_deal_.add_comment(com=com,id=activity['id'],type_c=type)
        return redirect(url_for('event_detail',event_name=event_name))


    return render_template('event-single.html',event=event,activity=activity,comments=comments,form=comment,event_name=event_name)


@app.route('/events')
def events():
    event = db_deal_.get_activity()
    activity = db_deal_.get_event()
    return render_template('events.html',event=event,res=activity)



@app.route('/portfolio')
def portfolio():
    event = db_deal_.get_activity()
    stories = db_deal_.get_stories()
    return render_template('portfolio-mixed.html',event=event,stories=stories)
@app.route('/gallery')
def gallery():
    event = db_deal_.get_activity()
    stories = db_deal_.get_stories()
    return render_template('gallery-mixed.html',event=event,stories=stories)
@app.route('/blog')
def blog():
    event = db_deal_.get_activity()
    news = db_deal_.get_news()
    return  render_template('blog.html',event=event,news=news)
@app.route('/blog/<new_name>',methods=['post','get'])
def blog_detail(new_name):
    event = db_deal_.get_activity()
    new_detail = db_deal_.get_new_by_name(new_name)
    type_c =2
    comments = db_deal_.get_comments(id=new_detail['id'],type_c=type_c)
    comment = Comment()
    if comment.validate_on_submit():
        com = comment.get_comment()

        db_deal_.add_comment(com=com, id=new_detail['id'], type_c=type_c)
        return redirect(url_for('blog_detail',new_name=new_name))
    return  render_template('blog-single.html',event=event,new_name=new_name,new = new_detail,comments=comments,form=comment)
