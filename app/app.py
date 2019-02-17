from flask import Flask, render_template, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/holiday', methods=['POST'])
def holiday():
	country = request.form['country']
	resp = requests.get('https://holidayapi.com/v1/holidays?key=25cdcb8e-9da8-4d95-9383-fd41dd2404eb&country='+country+'&year=2018')
	json_object = resp.json()
	data = json_object['holidays']
	# data = json_object['holidays']['name'] 
	return render_template('holiday.html', data=data)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

