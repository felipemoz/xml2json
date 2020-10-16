import json
import xmltodict
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
	return jsonify(health=True)

@app.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': 'Not Found: ' + request.url}
    resp = jsonify(message)
    resp.status_code = 404
    return (resp)

@app.route('/xml2json', methods=['POST'])
def delete_user(xmlString):
	
	try:
		converted = json.dumps(xmltodict.parse(xmlString), indent=4)
		return (jsonify(converted))
	except Exception as e:
		return (jsonify(error='parser content', exc=e))


if __name__ == '__main__':
    app.run()