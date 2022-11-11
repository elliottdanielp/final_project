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