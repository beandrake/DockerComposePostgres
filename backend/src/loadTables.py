


def load_tables(cursor, timestamp, fullRecords):
	_load_temp_table(cursor, timestamp, fullRecords)
	
	
def _load_temp_table(cursor, timestamp, fullRecords):
	# Make temp table for all records from datafile
	query="""
		CREATE TEMP TABLE full_records (
			id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
			itemType VARCHAR(255),
			compatibility VARCHAR(255),
			rerolled BOOL,
			avg FLOAT,
			stddev FLOAT,
			min INT,
			max INT,
			pop INT,
			median INT,
			uploaded TIMESTAMP
		);
	"""
	cursor.execute(query)

	# populate with unfiltered data
	query="""
		INSERT INTO full_records (
			itemType, compatibility, rerolled, avg, 
			stddev, min, max, pop, median, uploaded
		)
		VALUES (
			%(itemType)s, %(compatibility)s, %(rerolled)s, %(avg)s,
			%(stddev)s, %(min)s, %(max)s, %(pop)s, %(median)s, %(timestamp)s
			);
	"""
	for record in fullRecords:
		record["timestamp"] = timestamp
		cursor.execute(query, record)


	# Optional verification output
	query="""
		SELECT * FROM full_records;
	"""
	cursor.execute(query)

	result = cursor.fetchone()
	while result is not None:
		print(result)
		result = cursor.fetchone()




def _load_weapon_type_table(cursor):
	# Make weapon_types table
	query="""
		CREATE TABLE weapon_types (
			id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
			description VARCHAR(255) UNIQUE
		);
	"""
	cursor.execute(query)


	# populate from raw data
	query="""
		INSERT INTO weapon_types (description)
		SELECT DISTINCT description
		FROM full_records;
	"""
	cursor.execute(query)


	# Optional verification output
	query="""
		SELECT * FROM full_records;
	"""
	cursor.execute(query)

	result = cursor.fetchone()
	while result is not None:
		print(result)
		result = cursor.fetchone()





