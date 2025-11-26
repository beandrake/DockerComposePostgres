from db import create_connection
from getFile import get_and_parse_data
from loadTables import load_tables

# PostgreSQL
DEFAULT_DATABASE = 'postgres'
DEFAULT_USER = 'postgres'
SUPERUSER_PASSWORD = open(r'/run/secrets/db_password').read()

# Docker
DB_PORT_OUTSIDE = '5432'
DB_PORT_INSIDE = '5432'		# ports set in docker-compose.yml
DB_HOST = 'db'				# the name of the service from docker-compose.yml


# create connection to database
connection = create_connection(
	DEFAULT_DATABASE,
	DEFAULT_USER,
	SUPERUSER_PASSWORD,
	DB_PORT_OUTSIDE,
	DB_HOST
)

# get data from web endpoint
rivenData = get_and_parse_data()

# connect to Postgres container
cursor = connection.cursor()

# load tables with data from the web endpoint
load_tables(cursor, rivenData["timestamp"], rivenData["records"])




