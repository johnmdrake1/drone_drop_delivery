'''
Am going to use one file for backend functionality, running the server, Flask, etc. for now. Subject to restructuring later.
'''

import flask

#Webapp using flask stored in variable called app
app = flask.Flask(__name__, static_folder="../static", template_folder="../templates")


#Start by rendering landing page

#Default URL
@app.route("/")
@app.route("/landing")
def landing():
	print("Rendering home/landing page...")
	return flask.render_template("landing.html")





app.run()