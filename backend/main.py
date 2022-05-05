'''
Am going to use one file for backend functionality, running the server, Flask, etc. for now. Subject to restructuring later.
'''

from flask import Flask, render_template, request, url_for, flash, redirect

#Webapp using flask stored in variable called app
app = Flask(__name__, static_folder="../static", template_folder="../templates")


#Start by rendering landing page

#Default URL
@app.route("/")
@app.route("/landing", methods=['POST', 'GET'])
def landing():
	print("Rendering home/landing page...")
	print(request.args.get("locality"))
	return render_template("landing.html")


