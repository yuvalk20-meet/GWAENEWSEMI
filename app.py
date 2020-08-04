from flask import Flask, render_template,url_for,request,redirect


app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/insta')
def insta():
	return render_template("services.html")

@app.route('/change')
def cases():
	return render_template("cases.html")

@app.route('/challenge')
def challenge():
	return render_template("blog.html")



if __name__ == '__main__':
   app.run(debug = True)

