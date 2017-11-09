;; Scheme's define macro defines a macro function which creates 
;;  a list of expression and evaluates it. 

;;  The first examples shows how macro is defined. It is going to create a list 
;;  (begin expr expr), and evaluates it.  


;; Macro's evaluation procedure : 
;; 		evaluate the operator sub-expression -> 
;; 		call the macro without evaluating it -> 
;; 		evaluate the expression

(define-macro (twice expr)
	(list 'begin expr expr))

(define-macro (check expr) (list 'if expr ''passed 
	(list 'quote (list 'failed: expr))))

;; Implement the for loop using macro

;; for loop is kinda like the map function 
;; but map function is a bit tedious
(define (map fn vals)
	(if 
		(null? vals)
		()
		(cons (fn (car vals)) (map fn (cdr vals)))
	)
)

;; for loop
(define-macro
	(for sym vals expr)
		(list 'map (list 'lambda (list sym) expr) vals)	
)