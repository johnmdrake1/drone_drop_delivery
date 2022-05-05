'''
Am going to use one file for backend functionality, running the server, Flask, etc. for now. Subject to restructuring later.
'''

from flask import Flask, render_template, request, url_for, flash, redirect, session

#Webapp using flask stored in variable called app
app = Flask(__name__, static_folder="../static", template_folder="../templates")


#Start by rendering landing page

#Default URL
@app.route("/")
@app.route("/landing", methods=['POST', 'GET'])
def landing():
	print("Rendering home/landing page...")
	drone_address = request.args.get("ship-address")
	cust_name = request.args.get("cust-name")
	if drone_address != None:
		if cust_name != None:
			return redirect(url_for("confirm", drone_address=drone_address, cust_name=cust_name))
	return render_template("landing.html")

#confirmation page
@app.route("/confirm", methods=['POST', 'GET'])
def confirm():
	drone_address=request.args.get('drone_address', None)
	cust_name=request.args.get('cust_name', None)
	return render_template("confirm.html", drone_address=drone_address,cust_name=cust_name)


