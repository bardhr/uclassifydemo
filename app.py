#!flask/bin/python
import requests
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

api_key_read = 'AIucSvHtAYew'
api_key_write = 'CwRWR3gJnoou'


@app.route('/classify', methods=['POST'])
def classify_text():
	if not request.json or not 'text' in request.json:
		abort(400)
	url = 'https://api.uclassify.com/v1/uclassify/sentiment/classify'
	data = []
	data.append(request.json['text'])
	response = requests.post(url, headers={'Authorization':'Token AIucSvHtAYew'}, json = {'texts' :  data }).json()
	return jsonify(response), 201



@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(debug=True)
	print('asdf')