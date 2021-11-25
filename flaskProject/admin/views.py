

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from . import admin
from .models import user
from .forms import LoginForm, db_add
from app import db_deal_,file

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = user.query.filter_by(username=form.username.data).first()
        if u is None or not u.verify_password(form.password.data):
            flash('无效的用户名或密码')

            return redirect(url_for('admin.login'))

        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin.index')
        # 重定向至首页
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html', title='Login', form=form)


@admin.route('/index',methods=['GET', 'POST'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('admin.login'))
    return render_template('admin/index.html')

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出了！')
    return redirect(url_for('admin.login'))

@admin.route('/table/<db_name>',methods=['GET', 'POST'])
def table(db_name):
    if not current_user.is_authenticated:
        return redirect(url_for('admin.login'))
    db_list = db_deal_.get_attributes(db_name)
    len_db_list = len(db_list)
    db_dic = db_deal_.get_db_by_name(db_name)
    db_form = db_add()
    if db_form.validate_on_submit():
        m = db_form.get_content()
        print(m)
        #if db_form.img_path.data:
        filename = db_form.img_path.data
        print(filename)
        #db_form.img_path.data.save('images/'+db_name+'/'+filename)
        flash('上传成功')
        print(db_form.errors)

    else:
        m = db_form.get_content()
        path = '../static/images/'+db_name+'/'
        if m['name'] != None:
            if m['img_path'] != None:
                filename = secure_filename(db_form.img_path.data.filename)

                file.save(db_form.img_path.data,db_name)

                path = path +filename
                print(path)
                m['img_path'] = path
            if m['img_path_small'] != None:
                filename = secure_filename(db_form.img_path_small.data.filename)
                path = path + filename
                print(path)
                file.save(db_form.img_path.data, db_name)
                m['img_path_small']=path
            flag = db_deal_.add_db_by_name(db_name=db_name,dic=m)
            if flag == 1:
                flash('添加成功')

            else:
                flash('添加失败')
            return redirect(url_for('admin.table', db_name=db_name))

    return render_template('admin/tables.html',db_list=db_list,len_db = len_db_list,db_dic = db_dic,db_name=db_name,form=db_form)