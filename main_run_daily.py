# ====================================================================================================
# Python main script
# ----------------------------------------------------------------------------------------------------

try:
	print('Job started')
	# import sub_warn_me

	# Part 1
	print('run_api__delisted_companies.py')
	import run_api__delisted_companies
	print('run_api__historical_dividends.py')
	import run_api__historical_dividends

	# Part 2
	print('run_etl__delisted_companies.py')
	import run_etl__delisted_companies
	print('run_etl__historical_dividends.py')
	import run_etl__historical_dividends

	print('Job finished')
	# sub_warn_me.send_mail_with_text('JOB_PASSED: fmp_ingestion', 'complete')

except Exception:
	print('Job failed with error')
	import traceback
	error_message = traceback.format_exc()
	print(error_message)
	# sub_warn_me.send_mail_with_text('JOB_FAILED: fmp_ingestion', error_message)

