; https://inst.eecs.berkeley.edu/~cs61a/fa19/lab/lab11/

(define (repeatedly-cube n x)
  ; Cubes the given value x n times.
    (if (= 0 n)
        x
        (let 
            ((y (repeatedly-cube (- n 1) x)))
            (* y y y)))
)


(define-macro (def func bindings body)
  ; Simulates a python def statement
  `(define ,func (lambda ,bindings ,body))
)

; Optional Problems

(define-macro (switch expr cases)
    ; Takes in an expression expr and a list of pairs, cases, where the first element of the pair is some value and the second element is a single expression.
    ; switch will evaluate the expression contained in the list of cases that corresponds to the value that expr evaluates to.
    (list 'if (list '= expr (car (car cases)))
          (car (cdr (car cases)))
          (list 'switch expr (cdr cases)))
)

; Lab12

; From Disc11
(define (combine-with f xs ys)
    ; Combines the respective elements of two streams using the combiner function f.
    (if (or (null? xs) (null? ys)) nil
        (cons-stream
            (f (car xs) (car ys))
            (combine-with f (cdr-stream xs) (cdr-stream ys))))
)

(define (partial-sums s)
  ; Returns a steram where the nth element is the cumulative sum of elements upto n in stream s.
  (define partial (cons-stream (car s) (combine-with + (cdr-stream s) partial)))
  partial
)


; Dragon Curve

(define (flatmap f x)
  ; Takes in a function and a list and concatenates the result of mapping the function on the list to the list.
  (append x (map f x))
)

(define (expand lst)
  'YOUR-CODE-HERE)

(define (interpret instr dist)
  'YOUR-CODE-HERE)

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))
