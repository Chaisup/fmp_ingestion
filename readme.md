## FMP Ingestion Workshop
My Solution for the Assignment of KKP - Data Engineer Application


### About
This workshop will use the following link to test data ingestion from a free financial data API.
The goal is to store data from this API into the local database.
- Financial Modeling Prep [FMP]

There are 2 example tables for the demo.
- Delisted Companies
- Historical Dividends


### Pre-requisites
This workshop requires the following local setup.
- Python 3.10.6 | [python.org]
- MySQL Workbench 8.0 | [freecodecamp.org]
- Visual Studio Code | [vsc]


### Solution Concept
This workshop provides a set of Python scripts to run data ingestion in 3 layers.

1> Main script
We can schedule it to run daily to run all the work.
- main_run_daily.py

2> Working scripts in the main script
- run_api__delisted_companies.py
- run_api__historical_dividends.py
- run_etl__delisted_companies.py
- run_etl__historical_dividends.py

3> Supporting scripts called from the working scripts
These are designed to be generic and can be reused for the same task.
There are 2 tasks of the ingestion work.
- sub_api__source_to_staging__fmp.py
- sub_etl__staging_to_dw.py


### Solution Implementation
Here are the summary steps.

1> Use MySQL Workbench to create 4 tables. (This is an initial step.)
- create_tables__fmp.sql

2> Run the main script.

3> Test the result using SQL as follows.

```sql
-- test_query_1
select * from kkp_staging.fmp__delisted_companies__daily_staging;
select * from kkp_staging.fmp__historical_dividends__daily_staging;
select * from kkp_dw.fmp__delisted_companies__daily_update order by 1 desc, 2;
select * from kkp_dw.fmp__historical_dividends__daily_update order by 1 desc, 2;
```

```sql
-- test_query_2
select delisted_date, count(1) as cnt, max(_sys_record_time) as latest_sys_record_time
from kkp_staging.fmp__delisted_companies__daily_staging 
group by 1 order by 1 desc;

select date, count(1) as cnt, max(_sys_record_time) as latest_sys_record_time
from kkp_staging.fmp__historical_dividends__daily_staging
group by 1 order by 1 desc;

select delisted_date, count(1) as cnt, max(_sys_record_time) as latest_sys_record_time
from kkp_dw.fmp__delisted_companies__daily_update
group by 1 order by 1 desc;

select date, count(1) as cnt, max(_sys_record_time) as latest_sys_record_time
from kkp_dw.fmp__historical_dividends__daily_update
group by 1 order by 1 desc;
```


### Testing & Demo

![cap1](https://github.com/Chaisup/fmp_ingestion/blob/main/cap_demo_mysql_1.png)

![cap2](https://github.com/Chaisup/fmp_ingestion/blob/main/cap_demo_mysql_2.png)

![cap3](https://github.com/Chaisup/fmp_ingestion/blob/main/cap_demo_python.png)


[//]: # (These are reference links. Credit: https://dillinger.io/)
	[FMP]: <https://site.financialmodelingprep.com/developer/docs/>
	[python.org]: <https://www.python.org/downloads/release/python-3106/>
	[freecodecamp.org]: <https://www.freecodecamp.org/news/how-to-install-mysql-workbench-on-windows/>
	[vsc]: <https://code.visualstudio.com/download>

