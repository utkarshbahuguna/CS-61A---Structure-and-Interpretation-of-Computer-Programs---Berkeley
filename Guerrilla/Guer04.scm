; https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/guer04.pdf

; Tail Recursion

; 1.1

(define (mult x y)
    ; Multiplies x by y
    (if (= 0 y)
        0
        (+ x (mult x (- y 1)))
    )
)
; Not tail recrusive, because the recursive call is a part of a tail context.

; Tail recrursive version

(define (product x y)
    (define (prod-tail x y prod)
        (if (= 0 y)
            prod
            (prod-tail x (- y 1) (+ prod x)))
    )
    (prod-tail x y 0)
)


(define (true1 n)
    ; Always evaluates to true assuming n is positive
    (if (= n 0)
    #t
    (and #t (true1 (- n 1))))
)
; Tail recursive because and is in the tail context of if and the recursive call is in the tail context of and


(define (true2 n)
    ; Always evaluates to true assuming n is positive
    (if (= n 0)
    #t
    (and #t (true2 (- n 1)) #f))
)
; Not tail recursive because and is in the tail context of if but the recursive call is not in the tail context of and;
; Will always evaluate to false


(define (contains lst x)
    ; Returns true if x is in lst
    (cond
        ((null? lst)            #f)
        ((equal? (car lst) x)   #t)
        ((contains (cdr lst) x) #t)
        (else                   #f)       
        )
)
; Not tail recursive; because the recursive calls are in the predicate part of cond while the expression parts are the tail contexts


; Tail recursive version

(define (contains-t lst x)
    ; Returns true if x is in lst
    (cond
        ((null? lst)            #f)
        ((equal? (car lst) x)   #t)
        (else                   (contains-t (cdr lst) x))       
        )
)


; 1.2

(define (sum-satisfied-k lst f k)
    ; Tail recursive procedure which takes in a list, a one-argument predicate procedure f and an integer k
    ; and returns the sum of the first k elements of lst that satisfy f. If there are not k such elements, return 0.
    (define (sum-s-tail lst f k result)
        (cond
            ((= k 0)            result)
            ((null? lst)        0)
            ((f (car lst))      (sum-s-tail (cdr lst) f (- k 1) (+ result (car lst))))
            (else               (sum-s-tail (cdr lst) f k result))
            )
    )
    (sum-s-tail lst f k 0)
)

; 1.3

(define (remove-range lst i j)
    ; Tail recursive procedure which returns a new list containing the elements of list lst except the ones from index i to j. Assume j > i and j < length of lst.
    (define (remove-range-tail lst i j non-removed)
        (cond
            ((and (= i 0) (= j -1))     (append non-removed lst))
            ((= i 0)                    (remove-range-tail (cdr lst) i (- j 1) non-removed))
            (else                       (remove-range-tail (cdr lst) (- i 1) (- j 1) (append non-removed (list (car lst)))))
        )
    )
    (remove-range-tail lst i j nil)
)


; 3.2 Create a new special form (when <conditon> <expr1> <expr2> <expr3> ... )
; where if the condition is not false, all the subsequent operands are evaluated in order
; and the value of the last expression is returned. Otherwise the entire when expression evaluates to okay.

; implementation without using quasiquotes
(define-macro (when condition . exprs)
    (list 'if condition (cons 'begin exprs) ''okay)
)

; implementation using quasiquotes
(define-macro (when-q condition . exprs)
    `(if ,condition ,(cons 'begin exprs) 'okay)
)


; GUER05

; 1.2
(define (merge s1 s2)
    ; Takes in two sorted infinite streams and returns a new infinite stream containing all the elements from both streams, in sorted order.
    (if (> (car s1) (car s2))        
        (cons-stream (car s2) (merge s1 (cdr-stream s2)))
        (cons-stream (car s1) (merge (cdr-stream s1) s2)))
)