<<<<<<< HEAD
from flask import render_template
=======

from flask import Flask, render_template,url_for,request,redirect
>>>>>>> 498b87157f325fa73522f509da46109776267106


app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

<<<<<<< HEAD
	if __name__ == "__main__":        
    app.run()

=======
if __name__ == '__main__':
   app.run(debug = True)
>>>>>>> 498b87157f325fa73522f509da46109776267106
