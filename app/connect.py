import pyodbc
import os

db_server = os.getenv('DB_SERVER')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_NAME')
db_encrypt = os.getenv('DB_ENCRYPT')
db_trust_certificate = os.getenv('DB_TRUST_CERTIFICATE')
db_timeout = os.getenv('DB_TIMEOUT')
db_driver = os.getenv('DB_DRIVER')
app_port = os.getenv('APP_PORT')

connection = ('DRIVER=%s;SERVER=%s;DATABASE=%s;Uid=%s;Pwd=%s;Encrypt=%s;TrustServerCertificate=%s;Timeout=%s' % (db_driver, db_server, db_database, db_user, db_password, db_encrypt, db_trust_certificate, db_timeout ))

print('odbc:' + connection)

conn = pyodbc.connect(connection)
cursor = conn.execute("select * from tbl_user")
print(cursor.fetchall())