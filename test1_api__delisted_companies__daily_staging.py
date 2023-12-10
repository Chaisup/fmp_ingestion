# ====================================================================================================
# Python script to download data from an API and ingest into a staging table in MySQL
# ----------------------------------------------------------------------------------------------------
# Import

from datetime import datetime
import requests
import pandas as pd
import mysql.connector


# ----------------------------------------------------------------------------------------------------
# Declare

# API
api_var = 'delisted-companies?page=0'
api_url = f'https://financialmodelingprep.com/api/v3/{api_var}&apikey=VeF5THZjZC1SznBwCsexx5m6W31A9oQR'
api_columns = {
	'symbol':'symbol',
	'companyName':'company_name',
	'exchange':'exchange',
	'ipoDate':'ipo_date',
	'delistedDate':'delisted_date'
}

# MySQL
host = 'localhost'
user = 'root'
password = '1234'
database = 'kkp_staging'
table_name = 'fmp__delisted_companies__daily_staging'
sys_columns = [
	'_sys_record_info',
	'_sys_record_time'
]


# ----------------------------------------------------------------------------------------------------
# Run

# Call API
print('Downloading API Data')
api_response = requests.get(api_url).json()
api_end_time = datetime.strftime(datetime.now(),'%Y-%m-%d %X')

# Prepare columns
df = pd.DataFrame(api_response)
df.rename(index=str, columns=api_columns, inplace=True)
df[sys_columns[0]] = 'api_var: '+api_var
df[sys_columns[1]] = api_end_time

# Create a connection to the MySQL database
print('Connecting MySQL')
connection = mysql.connector.connect(
	host=host,
	user=user,
	password=password,
	database=database
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Make a query "insert into table_name (column1, column2, column3) values (%s, %s, %s)"
print('Querying: Insert')
query_part1 = str(list(api_columns.values())+sys_columns).replace('[','(').replace(']',')').replace("'","")
query_part2 = '(' + ((r'%s, '*(len(api_columns)+len(sys_columns)))+'z').replace(', z',')')
query = f"insert into {table_name} {query_part1} values {query_part2}"

# Execute the query
cursor.executemany(query, df.values.tolist())

# Commit and close
connection.commit()
cursor.close()
connection.close()

print('Completed')

