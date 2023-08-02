#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from main import app

#Create config to connect MYSQL database with credentials 
mysql =MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'lib_mngt'

app.secret_key = 'ticket_manager'

mysql.init_app(app)