; https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc09.pdf

; 4.1

(define (factorial x)
    (if (= x 0)
        1
        (* x (factorial (- x 1))))
)

; 4.2

(define (fib n)
    ; Returns the nth fibonacci number

    (cond ((= n 0) 0) ((= n 1) 1) (else (+ (fib (- n 1)) (fib (- n 2)))))
)

; 5.1

(define (my-append a b)
    ; Takes two lists and concatenates them
    (if (null? a)
        b
        (cons (car a) (my-append (cdr a) b)))
)

; 5.2

(define (replicate x n)
    ; Returns a list with element x repeated n times
    (if (= n 0)
        nil
        (cons x (replicate x (- n 1))))
)

; 5.3 Run-length encoding

(define (uncompress s)
    ; Takes a run-length encoded compressed version of a sequence and retuns the expanded original version
    (if (null? s)
        nil
        (my-append (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s))))
)


; 6.1

(define (map fn lst)
    ; Takes a procedure fn and applies it to every element of list lst.
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map fn (cdr lst))))
)

; 6.2 Fill in a Tree ADT

(define (make-tree label branches) 
    (cons label branches)
    )

(define (label tree)
    ; Returns the label at the root node of tree
    (car tree)
)

(define (branches tree)
    (cdr tree)
)

; 6.3 Assuming the entries in a tree are all numbers, write a function to sum up the entries of a tree

(define (tree-sum tree)
    (if (null? (branches tree))
        (label tree)
        (+ (label tree) (lst-sum (map tree-sum (branches tree)))))
)

(define (lst-sum lst)
    ; Returns the sum of elements of lst
    (if (null? lst)
        0
        (+ (car lst) (lst-sum (cdr lst))))
)