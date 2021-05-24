; https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc10.pdf

; 3.2

(define (sum lst)
    ; Tail recursive function which returns the numerical sum of all values in lst. Assume list contains only numbers and there are no nested lists.
    (define (sum-tail lst result)
        (if (null? lst)
            result
            (sum-tail (cdr lst) (+ result (car lst))))
    )
    (sum-tail lst 0)
)

; 3.3

(define (fib n)
    ; Tail recursive function which returns the nth fibonacci number.
    (define (fib-sofar i curr next)
        (if (= i n)
            curr
            (fib-sofar (+ i 1) next (+ curr next)))
    )
    (fib-sofar 0 0 1)
)

; 4.1

(define (reverse lst)
    ; A tail recursive function that reverses a list.
    (define (reverse-sofar lst lst-sofar)
        (if (null? lst)
            lst-sofar
            (reverse-sofar (cdr lst) (cons (car lst) lst-sofar)))
    )
    (reverse-sofar lst nil)
)

(define (append a b)
    ; Tail recursive function which concatenates two lists together.
    (define (rev-append-tail a b)
        (if (null? a)
            b
            (rev-append-tail (cdr a) (cons (car a) b)))
    )
    (rev-append-tail (reverse a) b)
)

(define (insert n lst)
    ; Tail recursive function that takes in a number and a sorted list.
    ; The function returns a sorted copy with the number inserted in the correct position.
    (define (rev-insert lst rev-lst)
        (cond ((null? lst) (cons n rev-lst))
                ((> (car lst) n) (rev-insert (cdr lst) (cons (car lst) rev-lst))) 
                (else (append (reverse lst) (cons n rev-lst)))
        )
    )
    (rev-insert (reverse lst) nil)
)