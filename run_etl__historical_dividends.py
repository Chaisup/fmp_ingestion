# ====================================================================================================
# Python script to run ETL from a staging table to a dw table in MySQL
# ----------------------------------------------------------------------------------------------------
# Import

import sub_etl__staging_to_dw


# ----------------------------------------------------------------------------------------------------
# Declare

dict_input = {
	# MySQL
	'db_schema' : 'kkp_dw',
	'db_table' : 'fmp__historical_dividends__daily_update',

	'q_select' : """
	select
		date(date) as date
		, symbol
		, label
		, if(adj_dividend='', null, cast(adj_dividend as decimal(25,10))) as adj_dividend
		, if(dividend='', null, cast(dividend as decimal(25,10))) as dividend
		, if(record_date='', null, date(record_date)) as record_date
		, if(payment_date='', null, date(payment_date)) as payment_date
		, if(declaration_date='', null, date(declaration_date)) as declaration_date
		, _sys_record_info
		, _sys_record_time
	from kkp_staging.fmp__historical_dividends__daily_staging
	""",

	'q_where' : """
	where date
		between current_date - interval '7' day
			and current_date - interval '1' day
	"""
}


# ----------------------------------------------------------------------------------------------------
# Run

sub_etl__staging_to_dw.run(dict_input)

