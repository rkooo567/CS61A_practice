(define (add-to-all f lst)
	(define (helper f lst lst-so-far)
		(if (null? lst) 
			lst-so-far
			(helper 
				f 
				(cdr lst) 
				(append 
					lst-so-far
					(list 
						(cons 
							f 
							(car lst)
						)
					)
				)
			)
		)
	)
	(helper f lst '())
)

(define (sublists lst)
	(if 
		(null? lst)
			(list '())
			;else
			(append (sublists (cdr lst)) (add-to-all (car lst) (sublists (cdr lst)))) 

	)
)

(define (reverse lst)
	(if
		(null? lst)
			'()
			; else
			(append (reverse (cdr lst)) (list (car lst)))
	)
)

(define (reverse-recurse lst)
	(define (helper lst lst-so-far)
		(if 
			(null? lst)
				lst-so-far
				; else
				(helper (cdr lst) (cons (car lst) lst-so-far))
		)
	)
	(helper lst '())
)

(define (merge s0 s1)
	(cond 
		((null? s0) s1)
		((null? s1) s0)
		((> (car s0) (car s1)) (cons-stream s1 (merge s0 (cdr-stream s1))))
		((< (car s0) (car s1)) (cons-stream s0 (merge (cdr-stream s0) s1)))
		((eq? (car s0) (car s1)) (cons-stream s0 (merge (cdr-stream s0) (cdr-stream s1))))
	)
)

(define a (cons-stream 1 (cons-stream 2 nil)))
(define b (cons-stream 2 (cons-stream 3 (cons-stream 5 nil))))