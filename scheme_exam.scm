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


(define (concat a b)
	(if (not (null? a)) 
			(cons (car a) (concat (cdr a) b))
			; if a is null
			(if (not (null? b))
				(cons (car b) (concat '() (cdr b)))	
				; if b is also null
				nil
			)
	)
)

(define a '(1 2 3))
(define b '((4 5) 6 . 7))

(define (replicate x n)
	(if (eq? n 0)
		nil
		(cons x (replicate x (- n 1)))
	)
)

(replicate 5 3)

(define (uncompress s)
	(if (null? s)
		nil
		; else
		(concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))
	)
)

(print (uncompress '((a 1) (b 2) (c 3))))

; map function, which takes a preocdeure and applies it to every element in a given list.
(define (map fn lst)
	(if (null? lst)
		nil
		; if lst is not null
		(cons (fn (car lst)) (map fn (cdr lst)))
	)
)

(print (map (lambda (x) (+ 2 x)) '(2 3 4)))

; deep-map, which takes a procedure and applies to every element in a given nested list
(define (deep-map fn lst)
	(cond 
		; 1. if the list is the null
		((null? lst)
			nil
		)
		; 2. if the label is not the list, return it
		((not (pair? (car lst))) 
			(cons (fn (car lst)) (deep-map fn (cdr lst)))
		)
		; 3. if the label is pair
		(else
			(cons (deep-map fn (car lst)) (deep-map fn (cdr lst)))
		)
	)
)

(print (deep-map (lambda (x) (* x x)) '(1 2 3)))
(print (deep-map (lambda (x) (* x x)) '(1 ((4) 5) 9)))

(define (make-tree label branches) (cons label branches))
(define (label tree) (car tree))
(define (branches tree) (cdr tree))

; sums up the entries of a tree, assuming that the entries are all numbers
(define (tree-sum t)
	(+ (label t) (sum-lst (deep-map tree-sum (branches t))))
)

(define (sum-lst lst)
	(if (null? lst)
		0
		(+ (car lst) (sum-lst (cdr lst)))
	)
)

(define (fib n)
	(define (fib-tail n prev curr)
		(cond
			((= n 0) 0)
			((= n 1) 1)
			((= n 2) curr)
			(else (fib-tail (- n 1) curr (+ prev curr)))
		)
	)
	(fib-tail n 1 1)
)

(define (sum lst)
	(define (sum-tail n lst)
		(if (null? lst)
			n
			(sum-tail (+ n (car lst)) (cdr lst))
		)
	)
	(sum-tail 0 lst)
)

(define lst-for-sum '(3 2 4 5))

; insert, that takes in a number and a sorted list and returns 
; 	a sorted copy with the nuber inserted in the correct position
(define (insert n lst)
	(define (insert-tail n lst lst-so-far)
		(cond
			((null? lst) (cons n nil))
			((< n (car lst)) 
				(append lst-so-far (list n) lst)
			)
			(else
				(insert-tail n (cdr lst) (append lst-so-far (cons (car lst) nil)))
			)
		)
	)
	(insert-tail n lst '())
)


(define sorted-lst '(2 3 5 7 9 11))
(print (insert 4 sorted-lst))

(define (compute-rest n)
	(print 'evaluating!)
	(cons-stream n nil)
)

(define (has-even? s)
	(cond 
		((null? s) #f)
		((even? (car s)) #t)
		(else (has-even? (cdr-strem s)))

	)
)

; Wirte a function map-stream, which takes a function f and a stream s. It returns a new stream 
;	which has all the elements from s, but with f applied to each one.
(define (map-stream f s)
	(cond
		((null? s) nil)
		(else (cons-stream (f (car s)) (map-stream f (cdr-stream s))))
	)
)

(define nats (cons-stream 2 (cons-stream 3 (cons-stream 5 nil))))
(define evens (map-stream (lambda (x) (* x 2)) nats))

(define (next s n)
	(if (= n 0) (car s)
		(next (cdr-stream s) (- n 1))
	)
)

; Write a function range-stream which takes a start and end, 
;	and returns a stream that represents the integers between start and end - 1 (inclusive)
(define (range-stream start end)
	(define (range-helper n)
		(if 
			(= n end) 
				nil
				(cons-stream n (range-helper (+ n 1)))
		)
	)
	(range-helper start)
)

(define s (range-stream 1 5))

; Write a function slice which takes in a stream s, a start, and an end. 
;	It should return a Scheme list that contains the elements of s between index start and end, 
;	not including end. If the stream ends before end, you can return nil. 
(define (slice s start end)
	(cond 
		((= end 0) nil)
		((= start 0) (cons (car s) (slice (cdr-stream s) 0 (- end 1))))
		(else (slice (cdr-stream s) (- start 1) (- end 1)))
	)
)

(define (naturals n)
	(cons-stream n (naturals (+ n 1)))
)

(define nat (naturals 0))

; return the stream of values (f xs ys) 
(define (combine-with f xs ys)
	(if (or (null? xs) (null? ys))
		nil
		(cons-stream
			(f (car xs) (car ys))
			(combine-with f (cdr-stream xs) (cdr-stream ys))
		)
	)
)

(define evens (combine-with + (naturals 0) (naturals 0)))

(define factorials
	(cons-stream 1 (combine-with * (naturals 1) factorials))
)

(define fibs
	(cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
)

(define (pow n power)
	(define (pow-tail power-tail number-so-far)
		(if (= power-tail power)
				number-so-far
				(pow-tail (+ power-tail 1) (* number-so-far n))
		)
	)
	(pow-tail 0 1)
)

(define (exp x)
	(combine-with / (combine-with pow x (naturals 0)) factorials)
)

