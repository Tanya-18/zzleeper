import os
from flask import Flask,render_template,url_for

template_dir = os.path.abspath('../zzleeper/zzleeper/pages/templates')
print(template_dir)
static_dir = os.path.abspath('../zzleeper/zzleeper/pages/static')

app = Flask('__name__', template_folder=template_dir, static_folder=static_dir)

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html", title='welcome-page')




    