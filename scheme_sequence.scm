;; Implementation of sequence operations in Scheme

;; Map f over s
(define (map f s)
	(if (null? s)
		nil
		(cons 
			(f (car s))
			(map f (cdr s))
		)
	)
)

;; Filter s by f
(define (filter f s)
	(if (null? s) 
		nil
		; if s is not null
		(if (f (car s))
			(cons (car s) (filter f (cdr s)))
			; if filter does not work
			(filter f (cdr s))
		) 
	)
)

;; Reduce s using f and start value.
(define (reduce f s start)
	(if (null? s)
		start
		; if s is not null
		(reduce f (cdr s) (f start (car s)))
	)
)

(define (range a b)
	(if (>= a b) 
			nil 
			(cons a (range (+ a 1) b))
	)
)

(define (sum s)
	(reduce + s 0)
)

(define (prime? x)
	(if (<= x 1)
		false
		(null? (filter (lambda (y) (= 0 (remainder x y))) (range 2 x)))
	)
)

(define (sum-primes a b)
	(sum (filter prime? (range a b)))
)