CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

WITH
	ancestors(ancestor, descendent) AS (
		SELECT parent, child FROM parents UNION
		SELECT ancestor, child 
			FROM ancestors, parents
			WHERE parent = descendent
	)
	SELECT ancestor, descendent FROM ancestors WHERE descendent = "clinton";

CREATE TABLE odds AS 
	WITH 
		odds(n) AS (
			SELECT 1 UNION
			SELECT n + 2
				FROM odds
				WHERE n < 15
		)
	SELECT n from odds;

CREATE TABLE nouns AS
	SELECT "the dog" AS phrase UNION
	SELECT "the cat"		   UNION
	SELECT "the bird";

SELECT s.phrase || " chased " || o.phrase
	FROM nouns as s, nouns as o
	WHERE s.phrase != o.phrase;

WITH
	compounds(phrase, n) AS (
		SELECT phrase, 1 FROM nouns UNION
		SELECT subject.phrase || " that chased " || object.phrase, n + 1
			FROM compounds AS subject, nouns AS object
			WHERE subject.phrase != object.phrase AND  n < 2 
	)
SELECT s.phrase || " chased " || o.phrase
	FROM compounds AS s, nouns AS o;

CREATE TABLE pairs AS
	WITH
		i(n) AS (
			SELECT 1 UNION
			SELECT n + 1 FROM i WHERE n < 50
		)
	SELECT a.n AS x, b.n AS y FROM i AS a, i AS b WHERE a.n <= b.n;

SELECT x, y FROM pairs WHERE x * y = 24