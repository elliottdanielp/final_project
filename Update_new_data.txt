-- To remove old data, and insert new data from dataset2
truncate titanic_1;

-- to make sure table has no data
select * from titanic_1;
0 rows

-- After importing from Titanic-dataset2, using Import from PgAdmin
select count(1) from titanic_1;
1309