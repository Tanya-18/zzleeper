import os
from flask import Flask,render_template,url_for, flash, redirect
from zzleeper.forms import RegistrationForm, LoginForm

template_dir = os.path.abspath('../zzleeper/zzleeper/pages/templates')
print(template_dir)
static_dir = os.path.abspath('../zzleeper/zzleeper/pages/static')

app = Flask('__name__', template_folder=template_dir, static_folder=static_dir)

app.config['SECRET_KEY'] = '73098c1af888bfc7bc88a72e5a559f2c'

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html", title='welcome-page')

@app.route("/register", methods=['GET','POST']) 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('welcome'))
    return render_template('register.html', title='Register page', form=form)

@app.route("/login") 
def login():
    form = LoginForm()
    return render_template('layout_nav.html', title='Login page', form=form)





    