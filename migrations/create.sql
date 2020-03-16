create table period
(
	client_id varchar,
	month smallint,
	year smallint,
	value bigint,
	is_pay boolean
);

create table client
(
	id varchar,
	name varchar,
	payment decimal(10,2)
);
