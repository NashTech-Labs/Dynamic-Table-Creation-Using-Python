import mysql.connector
from mysql.connector import errorcode
import os

############# ENVIRONMENT VARIABLES ##############################

USER = os.environ.get("DBUSER")
PASSWORD = os.environ.get("DBPASSWORD")
HOST = os.environ.get("DBHOST")
PORT = os.environ.get("DBPORT")
DBNAME = os.environ.get("DBNAME")

###################################################################

config = {
  'user': USER,
  'password': PASSWORD,
  'host': HOST,
  'port': PORT,
  'database': DBNAME,
  'raise_on_warnings': True
}

try:
  def getConnection():
    cnx = mysql.connector.connect(**config)
    return cnx
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
