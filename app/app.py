from flask import Flask, render_template, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/holiday', methods=['POST'])
def holiday():
	country = request.form['country']
	
	resp = requests.get('https://holidayapi.com/v1/holidays?key=a7e448b9-c572-4a51-8fdc-282ecb77c33d&country='+country+'&year=2019&month=01&day=01')
	json_object = resp.json()
	data = str(json_object['holidays'][0]['name'])
	# data = json_object['holidays']['name'] 
	return render_template('holiday.html', data=data)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

