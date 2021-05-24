; https://inst.eecs.berkeley.edu/~cs61a/fa19/hw/hw09/


; Tail recursion

; From Disc11
(define (replicate x n)
    ; Returns a list with x repeated n times
    (if (= n 0)
        nil
        (cons x (replicate x (- n 1))))
)

; Define replicate-t to be tail recursive version of replicate

(define (replicate-t x n)
  (define (rep x n result)
    (if (= n 0)
      result
      (rep x (- n 1) (cons x result))
    )
  )
  (rep x n nil)
)

(define (accumulate combiner start n term)
  ; Combines the first n natural numbers using a two-argument commutative function, combiner, starting with start where term computes the nth term.
    (if (= n 0)
      start
      (combiner start (accumulate combiner (term n) (- n 1) term))
    )
)

(define (accumulate-tail combiner start n term)
  ; Combines the first n natural numbers using a two-argument commutative function, combiner, starting with start where term computes the nth term.
    (if (= n 0)
      start
      (accumulate combiner (combiner start (term n)) (- n 1) term)
    )
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  ; An implicitly defined infinite stream that contains the multiples of 3
  (cons-stream 0 (map-stream (lambda (x) (+ 3 x)) multiples-of-three))
)

; From Disc11
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


(define (nondecreastream s)
  ; Takes in a stream of numbers s and outputs a stream of lists,
  ; which overall has the same numbers in the same order but grouped into segments that are non-decreasing.
  (cond ((null? (cdr-stream s))                     (cons (car s) nil))
        ((> (car s) (car (cdr-stream s)))           (cons-stream (cons (car s) nil) (nondecreastream (cdr-stream s))))
        (else                                       (cons-stream (cons (car s) (car (nondecreastream (cdr-stream s)))) (cdr-stream (nondecreastream (cdr-stream s)))))
  )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))