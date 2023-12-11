# ====================================================================================================
# Python script to download data from an API and ingest into a staging table in MySQL
# ----------------------------------------------------------------------------------------------------
# Import

import sub_api__source_to_staging__fmp
from datetime import datetime, timedelta


# ----------------------------------------------------------------------------------------------------
# Declare

date_d1 = (datetime.today()-timedelta(1)).strftime('%Y-%m-%d')
date_d7 = (datetime.today()-timedelta(7)).strftime('%Y-%m-%d')

api_var = f'stock_dividend_calendar?from={date_d7}&to={date_d1}'
api_key = 'VeF5THZjZC1SznBwCsexx5m6W31A9oQR'

dict_input = {
	# API
	'api_var' : api_var,
	'api_url' : f'https://financialmodelingprep.com/api/v3/{api_var}&apikey={api_key}',
	'api_columns' : {
		'date':'date',
		'label':'label',
		'adjDividend':'adj_dividend',
		'symbol':'symbol',
		'dividend':'dividend',
		'recordDate':'record_date',
		'paymentDate':'payment_date',
		'declarationDate':'declaration_date',
	},
	# MySQL
	'db_schema' : 'kkp_staging',
	'db_table' : 'fmp__historical_dividends__daily_staging'
}


# ----------------------------------------------------------------------------------------------------
# Run

sub_api__source_to_staging__fmp.run(dict_input)

