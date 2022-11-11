create table titanic_1
as
(SELECT p.*,s.survived,s.pclass, s.parch, s.ticket, s.cabin, s.embarked, s.fare
FROM titanic_passenger p
LEFT OUTER JOIN titanic_passenger_ship s
ON p.passengerid = s.passengerid);