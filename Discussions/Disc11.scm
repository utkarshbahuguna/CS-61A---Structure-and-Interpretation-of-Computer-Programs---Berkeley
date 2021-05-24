; https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc11.pdf

; Macros

; 1.1

(define-macro (make-lambda expr)
    ; Returns a parameter-less lambda procedure with expr as its body.
    `(lambda () ,expr)
)

; 1.2

(define (replicate x n)
    ; Returns a list with x repeated n times
    (if (= n 0) nil
    (cons x (replicate x (- n 1))))
)

(define-macro (repeat-n expr n)
    ; Repeat the expression expr n times
    (list 'eval (list 'cons ''begin (list 'replicate (list 'quote expr) n)))
)

; 1.3

(define-macro (or-macro expr1 expr2)
    ; or's expr1 and expr2 together applying short-circuting rules.
    `(let ((v1 ,expr1))
        (if v1
            #t
            ,expr2))
)

; Streams

; 2.2 The rest of the stream is calculated in the second implementation while assigning rest.
; This means with each call to filter-stream the rest of the stream keeps getting computed for
; the full stream at best or in an endless recursive loop for infinite streams at worst.
; Rest is the whole filtered rest of stream instead of being a promise.

; 2.3

(define (map-stream f s)
    ; Retruns a new stream which has all elements of stream s with f applied to each one.
    (cons-stream (f (car s)) (map-stream f (cdr-stream s)))
)

; 2.4

(define (slice s start end)
    ; Returns a Scheme list containing the elements of stream s between index start and end (not included).
    ; If stream ends before end, return nil.
    
    (define (slice-tail s start end sliced)
        (cond ((or (> start end) (= start end)) sliced)
                ((null? s) nil)
                ((= start 0) (slice-tail (cdr-stream s) 0 (- end 1) (append sliced (list (car s)))))
                (else (slice-tail (cdr-stream s) (- start 1) (- end 1) sliced)))
    )
    (slice-tail s start end nil)
)

; 2.5

(define (combine-with f xs ys)
    ; Combines the respective elements of two streams using the combiner function f.
    (if (or (null? xs) (null? ys)) nil
        (cons-stream
            (f (car xs) (car ys))
            (combine-with f (cdr-stream xs) (cdr-stream ys))))
)

(define (naturals n)
    ; Returns the infinite stream of natural numbers starting at n
    (cons-stream n (naturals (+ n 1)))
)

(define factorials (cons-stream 1 (combine-with * (naturals 1) factorials)))

(define fibs (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))

(define (exp x)
    ; Returns a stream where the nth term is the degree-n polynomial expansion of e^x
    (begin (define xs (cons-stream x xs))
            (define x^i (combine-with expt xs (naturals 0)))
            (define term (combine-with / x^i factorials))
            (define result (cons-stream (car term) (combine-with + (cdr-stream term) result))))
            result
)


; Extra Questions

; 3.1 Use make-lambda macro to define make-stream and cdr-stream. Do not have to implement memoization

(define-macro (make-stream first second)
    (list 'cons first (list 'cons (list 'make-lambda second) 'nil))
)

(define (cdr-s stream)
    ((car (cdr stream)))
)

; 3.2

(define (filter-stream f s)
    ; Filters a stream s using fuction s
    (cond ((null? s) nil)
            ((f (car s)) (cons-stream (car s) (filter-stream f (cdr-stream s))))
            (else (filter-stream f (cdr-stream s))))
)

(define (sieve s)
    ; Takes in a stream of increasing numbers and
    ; returns a stream containing only those which are not multiples of an earlier number in the stream.
    (if (null? s) nil
        (cons-stream (car s) (sieve (filter-stream (lambda (x) (not (= 0 (remainder x (car s))))) (cdr-stream s)))))
)

(define primes (sieve (naturals 2)))