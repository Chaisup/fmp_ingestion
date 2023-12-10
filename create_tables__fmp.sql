-- Schema: kkp_staging

create table kkp_staging.fmp__delisted_companies__daily_staging (
	symbol varchar(255)
	, company_name varchar(255)
	, exchange varchar(255)
	, ipo_date varchar(255)
	, delisted_date varchar(255)
	, _sys_record_info varchar(255)
	, _sys_record_time timestamp
)
;

create table kkp_staging.fmp__historical_dividends__daily_staging (
	date varchar(255)
	, label varchar(255)
	, adj_dividend varchar(255)
	, symbol varchar(255)
	, dividend varchar(255)
	, record_date varchar(255)
	, payment_date varchar(255)
	, declarationDate varchar(255)
	, _sys_record_info varchar(255)
	, _sys_record_time timestamp
)
;


-- Schema: kkp_dw

create table kkp_dw.fmp__delisted_companies__daily_update (
	delisted_date date
	, symbol varchar(255)
	, company_name varchar(255)
	, exchange varchar(255)
	, ipo_date date
	, _sys_record_info varchar(255)
	, _sys_record_time timestamp
)
;

create table kkp_dw.fmp__historical_dividends__daily_update (
	date date
	, symbol varchar(255)
	, label varchar(255)
	, adj_dividend decimal(25,10)
	, dividend decimal(25,10)
	, record_date date
	, payment_date date
	, declarationDate date
	, _sys_record_info varchar(255)
	, _sys_record_time timestamp
)
;

