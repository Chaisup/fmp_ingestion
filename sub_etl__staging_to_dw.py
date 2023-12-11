# ====================================================================================================
# Python script to run ETL from a staging table to a dw table in MySQL
# ----------------------------------------------------------------------------------------------------
# Import

import mysql.connector


# ----------------------------------------------------------------------------------------------------
# Run

def run(dict_input):

	# Get Input
	db_host     = dict_input.get('db_host', 'localhost')
	db_user     = dict_input.get('db_user', 'root')
	db_password = dict_input.get('db_password', '1234')
	db_schema   = dict_input.get('db_schema')
	db_table    = dict_input.get('db_table')
	q_select    = dict_input.get('q_select')
	q_where     = dict_input.get('q_where')

	# ------------------------------------------------------------------------------------------------

	# Create a connection to the MySQL database
	print('Connecting MySQL')
	connection = mysql.connector.connect(
		host=db_host,
		user=db_user,
		password=db_password,
		database=db_schema
	)

	# Create a cursor object to execute SQL queries
	cursor = connection.cursor()

	# Make queries
	print('Querying: update-insert')
	q_delete = f"delete from {db_schema}.{db_table} {q_where}"
	q_insert = f"insert into {db_schema}.{db_table} {q_select} {q_where}"

	# Execute the queries
	cursor.execute(q_delete)
	cursor.execute(q_insert)

	# Commit and close
	connection.commit()
	cursor.close()
	connection.close()

	print('Completed')

