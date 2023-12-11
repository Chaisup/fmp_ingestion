# ====================================================================================================
# Python script to download data from an API and ingest into a staging table in MySQL
# ----------------------------------------------------------------------------------------------------
# Import

import sub_api__source_to_staging__fmp


# ----------------------------------------------------------------------------------------------------
# Declare

api_var = 'delisted-companies?page=0'
api_key = 'VeF5THZjZC1SznBwCsexx5m6W31A9oQR'

dict_input = {
	# API
	'api_var' : api_var,
	'api_url' : f'https://financialmodelingprep.com/api/v3/{api_var}&apikey={api_key}',
	'api_columns' : {
		'symbol':'symbol',
		'companyName':'company_name',
		'exchange':'exchange',
		'ipoDate':'ipo_date',
		'delistedDate':'delisted_date'
	},
	# MySQL
	'db_schema' : 'kkp_staging',
	'db_table' : 'fmp__delisted_companies__daily_staging'
}


# ----------------------------------------------------------------------------------------------------
# Run

sub_api__source_to_staging__fmp.run(dict_input)

