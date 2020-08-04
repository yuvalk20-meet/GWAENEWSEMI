from database import *
from flask import Flask, render_template,url_for,request,redirect
from flask import session as login_session
import requests, json , flask , Flask

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")


if __name__ == '__main__':
   app.run(debug = True)

