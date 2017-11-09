(define 
	(factorial n)
		(if
			(= n 1)
				1
				(* n (factorial (- n 1)))
		)
)

(define
	(fac-exp n)
		(if
			(= n 1)
				1
				(list '* n (fac-exp (- n 1)))
		)
)

(define 
	(fib n)
		(if
			(= n 1)
				0
				(if
					(= n 2)
						1
						(+ (fib (- n 1)) (fib (- n 2)))
				)
		)
)

(define
	(fib-exp n)
		(cond
			((= n 1) 0)
			((= n 2) 1)
			(else (list '+ (fib (- n 1)) (fib (- n 2))))
		)
)