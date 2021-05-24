; https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/guer03.pdf

; 1.3
(define (cat meow purr) (+ meow purr))

(define cat (lambda (meow purr) (+ meow purr)))

; 1.4

(define (sum-every-other lst)
    (cond ((null? lst) 0)
    (else (+ (car (cdr lst))
            (sum-every-other (cdr (cdr lst))))))
)

; 1.5

(define (sixty-ones lst)
    ; Returns the number of times 1 follows 6 in lst
    (if (null? lst) 0
        (+ (if (and (= (car lst) 6) (= (car (cdr lst)) 1)) 1 0)
            (sixty-ones (cdr lst))))
)

; 1.6

(define (no-elevens n)
    ; Returns a list of all distinct length-n lists of 1s and 6s that do not contain consecutive 1s.
    (cond ((= n 0) nil)
            ((= n 1) (cons '(6) (cons '(1) nil)))
            (else (append (map (lambda (lst) (cons 6 lst)) (no-elevens (- n 1))) 
                (map (lambda (lst) (cons 1 lst)) (filter (lambda (lst) (not (= (car lst) 1))) (no-elevens (- n 1)))))))
)

; 1.7

(define (remember f)
    ; Takes in f, a zero-argument function, and returns another function g.
    ; When called for the first time, g will call f and pass on its return value.
    ; When called subsequent times, g will remember its previous return value and return it directly without calling f again.
    (begin
    (define result nil)
    (define calls 0)
    (lambda ()
        (if (= calls 0)
            (begin
            (set! result (f))
            (set! calls (+ calls 1))
            result)
            result))) 
)

;;; Tests
    (define (f)
        (begin (print 'fcalled) 1)
        )

    (define g (remember f))
    ; (g)
    ; expect 'fcalled 1
    ; (g)
    ; expect 1
;

; 2.2

(define (better-append . args) ; (variadic args)
    ; Concatenates together an arbitrary number of lists passed in as arguments
    (if (null? args)
        nil
        (reduce my-append args))
)   


; From Disc09

(define (my-append a b)
    ; Takes two lists and concatenates them
    (if (null? a)
        b
        (cons (car a) (my-append (cdr a) b)))
)