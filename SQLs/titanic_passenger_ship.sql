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