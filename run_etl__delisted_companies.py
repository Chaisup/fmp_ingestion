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
	'db_table' : 'fmp__delisted_companies__daily_update',

	'q_select' : """
	select
		date(delisted_date) as delisted_date
		, symbol
		, company_name
		, exchange
		, if(ipo_date='', null, date(ipo_date)) as ipo_date
		, _sys_record_info
		, _sys_record_time
	from kkp_staging.fmp__delisted_companies__daily_staging
	""",

	'q_where' : """
	where delisted_date
		between current_date - interval '7' day
			and current_date - interval '1' day
	"""
}


# ----------------------------------------------------------------------------------------------------
# Run

sub_etl__staging_to_dw.run(dict_input)

