import psycopg2 as pg

def create_connection(db_name, db_user, db_password, db_port, db_host=None):
	kwargs = {
		'database': db_name,
		'user': db_user,
		'password': db_password,
		'port': db_port,
	}
	if db_host:
		kwargs['host']=db_host
	connection = None
	try:
		print("Connecting to PostgreSQL DB...")
		connection = pg.connect(**kwargs)
		print("Successfully connected to PostgreSQL DB.")
	except pg.OperationalError as e:
		print("Error when attempting to connect to PostgreSQL DB:\n" + str(e))
	return connection











