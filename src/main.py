import json
import xmltodict
from flask import Flask, jsonify, make_response, request
import sender from sender

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
def simple_convert(xmlString):
	
	try:
		content = json.dumps(xmltodict.parse(xmlString), indent=4)
		return (jsonify(content))

	except Exception as e:
		return (jsonify(error='parser content', exc=e))


@app.route('/xml2EventHub', methods=['POST'])
def xnl_2_event_hub(xmlString):
	
	try:
		content = json.dumps(xmltodict.parse(xmlString), indent=4)
		
		sender(content=content)

		return (jsonify(message='ok'))
	except Exception as e:
		return (jsonify(error='parser content', exc=e))


if __name__ == '__main__':
    app.run()