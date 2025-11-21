from getFile import get_and_parse_data
from db import create_connection
import time

# PostgreSQL
DEFAULT_DATABASE = 'postgres'
DEFAULT_USER = 'postgres'
SUPERUSER_PASSWORD = open(r'/run/secrets/db_password').read()

# Docker
DB_PORT_OUTSIDE = '5432'
DB_PORT_INSIDE = '5432'		# ports set in docker-compose.yml
DB_HOST = 'db'				# the name of the service from docker-compose.yml

MAX_STARTUP_SECONDS = 5



print( get_and_parse_data() )




connection = create_connection(
	DEFAULT_DATABASE,
	DEFAULT_USER,
	SUPERUSER_PASSWORD,
	DB_PORT_OUTSIDE,
	DB_HOST
)



cursor = connection.cursor()

query="""
	CREATE TABLE mascots (
		id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
		name VARCHAR(255)

	);
"""

cursor.execute(query)



query="""
	SELECT CURRENT_TIMESTAMP;
"""
cursor.execute(query)
result = cursor.fetchone()
myTime = result[0].strftime("%I:%M:%S")
print(myTime)

