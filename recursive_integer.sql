CREATE TABLE p AS 
	WITH
		i(n) AS (
			SELECT 1 UNION
			SELECT n + 1 FROM i WHERE n < 20
		)
	SELECT a.n AS a, b.n AS b, c.n AS c
		FROM i AS a, i AS b, i AS c
		WHERE b.n > a.n AND a.n*a.n + b.n*b.n = c.n*c.n;

SELECT a, b, c FROM p;

-- Fibonacci sequence
CREATE TABLE fibs AS
	WITH
		fib(previous, current) AS (
			SELECT 0, 1 UNION
			SELECT current, previous + current 
				FROM fib
				WHERE current <= 20
		)
	SELECT previous AS n FROM fib;

-- sum of perfect cubes
CREATE TABLE pairs AS
	WITH
		i(n) AS (
			SELECT 1 UNION
			SELECT n + 1 FROM i WHERE n < 50
		)
	SELECT a.n AS x, b.n AS y FROM i AS a, i AS b WHERE a.n <= b.n;

CREATE TABLE interests AS
	WITH
		cubes(x, y, cube) AS (
			SELECT x, y, x*x*x + y*y*y FROM pairs
		)
	SELECT a.x, a.y, b.x, b.y, a.cube AS sum_cubes
		FROM cubes AS a, cubes AS b
		WHERE a.x < b.x AND a.cube = b.cube;