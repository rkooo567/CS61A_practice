;; Implementation of sequence operations in Scheme
;; And Stream exercises.

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

;; Streams
(define s (cons-stream 1 (cons-stream 2 nil)))

(define t (cons-stream 1 (/ 1 0)))

(define (range-stream a b)
	(if (>= a b) nil (cons-stream a (range-stream (+ a 1) b)))
)

;; represents infinte number of sequence.
(define (int-stream start)
	(cons-stream start (int-stream (+ 1 start)))
)

;; count number of int-stream (s) from k
(define (prefix s k)
	(if (= k 0)
		()
		(cons (car s) (prefix (cdr-stream s) (- k 1)))
	)
)

;; Stream processing

;; square all the element in s
(define (square-stream s)
	(cons-stream 
		(* (car s) (car s))
		(square-stream (cdr-stream s))
	)
)

;; recursive stream

;; 1 1 1 1 1 1....
(define ones (cons-stream 1 ones))

;; combine two streams by separating each into car and cdr
(define (add-streams s t)
	(cons-stream 
		(+ (car s) (car s))
		(add-streams (cdr-stream s) (cdr-stream t))
	)
)

;; 1 2 3 4 5 .....
(define ints (cons-stream 1 (add-streams ones ints)))

;; higher order function
;; sequence operation with streams
;; Map f over s
(define (map-stream f s)
	(if (null? s)
		nil
		(cons-stream 
			(f (car s))
			(map-stream f (cdr-stream s))
		)
	)
)

;; Filter s by f
(define (filter-stream f s)
	(if (null? s) 
		nil
		; if s is not null
		(if (f (car s))
			(cons-stream (car s) (filter-stream f (cdr-stream s)))
			; if filter does not work
			(filter-stream f (cdr-stream s))
		) 
	)
)

;; Reduce s using f and start value.
(define (reduce-stream f s start)
	(if (null? s)
		start
		; if s is not null
		(reduce-stream f (cdr-stream s) (f start (car s)))
	)
)

;; a stream of primes
;; Sieve of Eratosthenes
;; The stream of integers not divisible by any k <= n is:
;; 1. The stream of integers not divisible by any k < n
;; 2. Filtered to remove any element divisible by n

(define (sieve s)
	(cons-stream 
		(car s)
		(sieve
			(filter-stream 
				(lambda (x) (not (= 0 (remainder x (car s)))))
				(cdr-stream s)
			)
		)
	)
)

(define primes (sieve (int-stream 2)))

;; promise
(define promise (let ((x 2)) (delay (+ x 1))))