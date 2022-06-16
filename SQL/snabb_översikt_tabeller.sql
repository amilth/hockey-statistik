select t.TABLE_NAME, t.TABLE_ROWS, count(c.COLUMN_NAME) as "Column_Count"
from INFORMATION_SCHEMA.TABLES as t
join INFORMATION_SCHEMA.COLUMNS as c 
	on c.TABLE_SCHEMA = t.TABLE_SCHEMA
	and c.TABLE_NAME = t.TABLE_NAME
where t.TABLE_SCHEMA = 'my_database'
group by t.TABLE_NAME, t.TABLE_ROWS;

select sum(t.TABLE_ROWS) as "Sum_Rows"
from INFORMATION_SCHEMA.TABLES as t
where t.TABLE_SCHEMA = 'my_database';