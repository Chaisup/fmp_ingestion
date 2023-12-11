# ====================================================================================================
# Python script to download data from an API and ingest into a staging table in MySQL
# ----------------------------------------------------------------------------------------------------
# Import

from datetime import datetime
import requests
import pandas as pd
import mysql.connector


# ----------------------------------------------------------------------------------------------------
# Run

def run(dict_input):

	# Get Input
	api_var     = dict_input.get('api_var')
	api_url     = dict_input.get('api_url')
	api_columns = dict_input.get('api_columns')
	db_host     = dict_input.get('db_host', 'localhost')
	db_user     = dict_input.get('db_user', 'root')
	db_password = dict_input.get('db_password', '1234')
	db_schema   = dict_input.get('db_schema')
	db_table    = dict_input.get('db_table')
	sys_columns = [
		'_sys_record_info',
		'_sys_record_time'
	]

	# ------------------------------------------------------------------------------------------------

	# Call API
	print('Downloading API Data')
	api_response = requests.get(api_url).json()
	api_end_time = datetime.strftime(datetime.now(),'%Y-%m-%d %X')

	# Prepare columns
	df = pd.DataFrame(api_response)
	df.rename(index=str, columns=api_columns, inplace=True)
	df[sys_columns[0]] = 'api_var: '+api_var
	df[sys_columns[1]] = api_end_time
	df.fillna('', inplace=True)

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
	print('Querying: truncate-insert')
	q_delete = f"delete from {db_schema}.{db_table}"
	q_insert_part1 = str(list(api_columns.values())+sys_columns).replace('[','(').replace(']',')').replace("'","")
	q_insert_part2 = '(' + ((r'%s, '*(len(api_columns)+len(sys_columns)))+'z').replace(', z',')')
	## q_insert : insert into target_table (column1, column2, column3) values (%s, %s, %s)
	q_insert = f"insert into {db_schema}.{db_table} {q_insert_part1} values {q_insert_part2}"

	# Execute the queries
	cursor.execute(q_delete)
	cursor.executemany(q_insert, df.values.tolist())

	# Commit and close
	connection.commit()
	cursor.close()
	connection.close()

	print('Completed')

