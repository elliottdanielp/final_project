-- total number of 'Titanic' tables

SELECT table_catalog, table_schema, table_name
  FROM information_schema.tables
 where table_name like 'titanic%'
 union
SELECT table_catalog, table_schema, table_name
  FROM information_schema.tables
 where table_name ='pass_boat_body' ;

-- 6 rows