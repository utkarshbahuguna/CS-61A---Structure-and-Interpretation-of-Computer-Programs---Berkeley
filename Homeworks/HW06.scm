; https://inst.eecs.berkeley.edu/~cs61a/fa19/hw/hw06/

;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  ; Return the second element of a list
  (car (cdr s))
)

(define (caddr s)
  ; Return the third element of a list
  (car (cddr s))
)

(define (sign x)
  ; Using a cond expression, define a procedure sign that takes in one parameter x and 
  ; returns -1 if x is negative, 0 if x is zero, and 1 if x is positive.
  (cond ((< x 0) -1) ((= x 0) 0) (else 1))
)

(define (square x) (* x x))

(define (pow b n)
  ; Raise b to the power of a nonnegative integer n (implement in O(log n))
  (if (= n 0) 1
    (if (even? n)
        (square (pow b (/ n 2)))
        (* b (square (pow b (/ (- n 1) 2))))))
)

(define (unique s)
  ; Takes in a list s and returns a new list containing the same elements as s with duplicates removed.
  (if (null? s)
    nil
    (cons (car s) (unique (filter (lambda (x) (not (= (car s) x))) (cdr s)))))
)

