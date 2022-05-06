'''
Am going to use one file for backend functionality, running the server, Flask, etc. for now. Subject to restructuring later.
'''
import requests

import json

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
	place_id = request.args.get("place-id")
	state = request.args.get("state")
	locality = request.args.get("locality")
	postcode = request.args.get("postcode")
	if drone_address != None:
		getplaceinfo(place_id)
		return redirect(url_for("confirm", drone_address=drone_address, cust_name=cust_name, state=state, locality=locality, postcode=postcode,place_id=place_id))
	return render_template("landing.html")

#confirmation page
@app.route("/confirm", methods=['POST', 'GET'])
def confirm():
	drone_address=request.args.get('drone_address', None)
	cust_name=request.args.get('cust_name', None)
	place_id=request.args.get('place_id', None)
	state = request.args.get("state", None)
	locality = request.args.get("locality", None)
	postcode = request.args.get("postcode", None)
	if request.method == 'POST':
		return redirect(url_for("result_map"))
	return render_template("confirm.html", drone_address=drone_address,cust_name=cust_name,state=state, locality=locality, postcode=postcode,place_id=place_id)


@app.route("/result_map", methods=['POST', 'GET'])
def result_map():
	return render_template("result_map.html")




def getplaceinfo(place_id):
	
	#https://developers.google.com/maps/documentation/places/web-service/details#maps_http_places_details_fields-py

	url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + place_id + "&fields=formatted_address&key=AIzaSyAbZRidkxGcoqNHugrihE0Lcwe_sk3mVHo"

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload).text

	data = json.loads(response)

	print(data['result']['formatted_address'])



