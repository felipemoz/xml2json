import pyodbc 
import os
import uuid
import hashlib
import json
from werkzeug.security import generate_password_hash
from flask import Flask, current_app, flash, jsonify, make_response, redirect, request, url_for



db_server = os.getenv('DB_SERVER')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_NAME')
db_encrypt = os.getenv('DB_ENCRYPT')
db_trust_certificate = os.getenv('DB_TRUST_CERTIFICATE')
db_timeout = os.getenv('DB_TIMEOUT')
db_driver = os.getenv('DB_DRIVER')
app_port = os.getenv('APP_PORT')
app_debug = os.getenv('APP_DEBUG')


connection = ('DRIVER=%s;SERVER=%s;DATABASE=%s;Uid=%s;Pwd=%s;Encrypt=%s;TrustServerCertificate=%s;Timeout=%s' % (db_driver, 
																												db_server, 
																												db_database, 
																												db_user, 
																												db_password, 
																												db_encrypt, 
																												db_trust_certificate, 
																												db_timeout ))

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

@app.route('/add', methods=['POST'])
def add_user():

		content = json.loads(request.data)

		_name = content['name']
		_email = content['email']
		_password = content['pwd']
		
		_hashed_password = generate_password_hash(_password, 'sha256')
		_user_id = uuid.uuid4()
		
		conn = pyodbc.connect(connection)
		cursor = conn.cursor()

		try:
				
			statement = ("INSERT INTO tbl_user(user_name, user_email, user_password, user_id) VALUES ('%s', '%s', '%s', '%s')" % (_name, _email, _hashed_password, _user_id))
			print(statement)

			cursor.execute(statement)
			conn.commit()			
	
			return jsonify(message='ok', user_id=_user_id)

		except Exception as e:
			return jsonify(error='fail to save records', exc=e, statement=statement)

		finally:
			pass
			cursor.close() 
			conn.close()

@app.route('/users', methods=['GET'])
def users():

	conn = pyodbc.connect(connection)
	cursor = conn.cursor()

	try:
		
		statement= ("SELECT * FROM tbl_user")
		
		cursor.execute(statement)
		
		colnames = ['user_id', 'user_name', 'user_email', 'user_password']
		data = {}

		for row in cursor.fetchall():
			colindex = 0
			for col in colnames:
				if not col in data:
					data[col] = []
				data[col].append(row[colindex])
				colindex += 1
		
		_type= type(data)

		return (jsonify(data))

	except Exception as e:
		return (jsonify(error='fail to list users', exc=e, statement=statement, type=_type))
	
	finally:
		
		cursor.close() 
		conn.close()

@app.route('/user/', methods=['GET'])
def user(id):
	conn = pyodbc.connect(connection)
	cursor = conn.cursor()

	try:
		
		statement= ("SELECT * FROM tbl_user where user_id = %s" % id)
		cursor.execute(statement)
		
		data = cursor.fetchone()
		_type= type(data)

		return (jsonify(data))

	except Exception as e:
		return (jsonify(error='fail to list user', id=id, exc=e, statement=statement, type=_type))
	
	finally:
		
		cursor.close() 
		conn.close()

@app.route('/update', methods=['POST'])
def update_user():
	content = json.loads(request.data)

	_name = content['name']
	_email = content['email']
	_password = content['pwd']
	_user_id = content['user_id']

	_hashed_password = generate_password_hash(_password, 'sha256')
	
	conn = pyodbc.connect(connection)
	cursor = conn.cursor()

	try:
		statement= ("'UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s'" % (_name, _email, _password, _user_id))
		cursor.execute(statement)
		conn.commit()			
	
		return jsonify(message='user updated', user_id=_user_id)

	except Exception as e:
		return (jsonify(error='fail to update user', id=_user_id, exc=e, statement=statement))
	
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/', methods=['POST'])
def delete_user(id):
	conn = pyodbc.connect(connection)
	cursor = conn.cursor()

	try:
		statement=("'DELETE FROM tbl_user WHERE user_id=%s" % (id))
		conn.commit()
		
		return jsonify(message='user updated', user_id=id)
	
	except Exception as e:
		return (jsonify(error='fail to update user', id=id, exc=e, statement=statement))

	finally:
		cursor.close() 
		conn.close()

if __name__ == '__main__':
    app.run(port=app_port, debug=app_debug)