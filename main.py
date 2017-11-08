#coding:utf-8

from flask import Flask, render_template
# from flask.ext.misaka import markdown
import subprocess
import shlex
import os

app = Flask(__name__)

@app.route('/')
def index():
    md_list = md_collect()

    return render_template('index.html',titlename="mainpage",md=md_list)

@app.route("/md/<md>")
def move_page(md):
    pandoc = "pandoc ./md/{0} --template=h5.html -t html5".format(md)

    p = subprocess.Popen(shlex.split(pandoc),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = p.communicate()

    return out.decode("utf-8")


def md_collect():
    md_list = os.listdir("./md")

    return md_list

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000,threaded=True)
