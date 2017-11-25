-- create a table animal for aggregation
CREATE TABLE animals AS
	SELECT "dogs" AS kind, 4 AS legs, 20 AS weight UNION
	SELECT "cat"         , 4        , 10           UNION
	SELECT "ferret"    	 , 4		, 10		   UNION
	SELECT "parrot"      , 2        , 6            UNION
	SELECT "penguin"     , 2        , 10           UNION
	SELECT "t-rex"       , 2        , 12000;

-- Aggregation statement
SELECT max(legs) FROM animals;
-- > 4

SELECT max(legs - weight) + 5 FROM animals;
-- > 1

SELECT max(legs), min(weight) FROM animals;
-- > 4|6

SELECT min(legs), max(weight) FROM animals WHERE name <> "t-rex";
-- > "dogs"

SELECT avg(legs) FROM animals;
-- > 3

SELECT count(legs) FROM animals;
-- > 6

SELECT count(kinds) FROM animals;
-- > same as the previous one 6

SELECT (count distinct legs) FROM animals;
-- > distinct is a keyword. It shows how many kinds of legs are there

SELECT max(weight), kind FROM animals;
-- > 12000|t-rex

SELECT min(kind), kind FROM animals;
-- > cat | cat -> min is going to be a condition

-- notice that sometimes it is not meaningful
-- ex)
SELECT avg(weight), kind FROM animals;

-- grouping
SELECT legs, max(weight) FROM animals GROUP BY legs;
-- > 4|20
-- > 2|12000

-- having clause filters the set of group that are aggregated.
SELECT weight/legs, count(*) FROM animals GROUP BY weight/legs HAVING count(*)>1;