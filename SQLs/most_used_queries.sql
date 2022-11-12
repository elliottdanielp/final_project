-- These has all the SQLs for the project Titanic

(1).
-- Table: public.titanic_passenger
-- DROP TABLE IF EXISTS public.titanic_passenger;

CREATE TABLE IF NOT EXISTS public.titanic_passenger
(
    passengerID integer NOT NULL,
    name text,
    sex text,
    age numeric,
    sibsp integer,
    CONSTRAINT titanic_main_pkey PRIMARY KEY (passengerID)
);

(2).
-- Table: public.titanic_passenger_ship
-- DROP TABLE IF EXISTS public.titanic_passenger_ship;

CREATE TABLE IF NOT EXISTS public.titanic_passenger_ship
(
    passengerid integer NOT NULL,
    name text,
    survived integer,
    pclass integer,
    parch integer,
    ticket text,
    cabin text,
    embarked text,
    fare numeric,
    CONSTRAINT passengerid_fk FOREIGN KEY (passengerid)
        REFERENCES public.titanic_passenger (passengerid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
);

(3).
-- Joining the above 2 tables, to create the main table
create table titanic_1
as
(SELECT p.*,s.survived,s.pclass, s.parch, s.ticket, s.cabin, s.embarked, s.fare
FROM titanic_passenger p
LEFT OUTER JOIN titanic_passenger_ship s
ON p.passengerid = s.passengerid);

(4).
-- this SQL shows the schema, and all the 'Titanic' tables in that schema
SELECT table_schema, table_name
  FROM information_schema.tables
 where table_name like 'titanic%'
 union
SELECT table_schema, table_name
  FROM information_schema.tables
 where table_name ='pass_boat_body' ;

-- 6 rows with output is below

"public"	"pass_boat_body"
"public"	"titanic_1"
"public"	"titanic_main"
"public"	"titanic_pass_boat"
"public"	"titanic_passenger"
"public"	"titanic_passenger_ship"