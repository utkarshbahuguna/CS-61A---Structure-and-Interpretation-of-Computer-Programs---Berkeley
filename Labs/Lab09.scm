; https://inst.eecs.berkeley.edu/~cs61a/fa19/lab/lab09/#q1

;; Scheme ;;

(define (over-or-under x y)
  ; Return -1 if x < y, 0 if x = y, and 1 if x > y
  (cond ((< x y) -1) ((= x y) 0) (else 1))
)

;;; Tests
  (over-or-under 1 2)
  ; expect -1
  (over-or-under 2 1)
  ; expect 1
  (over-or-under 1 1)
  ; expect 0
;

(define (filter-lst f lst)
  ; Returns a new list containing only elements of list lst that satisfy the perdicate f (in the same order).
  (if (null? lst)
    nil
    (if (f (car lst))
      (cons (car lst) (filter-lst f (cdr lst)))
      (filter-lst f (cdr lst))))  
)

;;; Tests
  (define (even? x)
    (= (modulo x 2) 0))
  (filter-lst even? '(0 1 1 2 3 5 8))
  ; expect (0 2 8)
;

(define (make-adder num)
  ; Returns a procedure which takes in a number x and returns x + num.
  (lambda (x) (+ num x))
)

;;; Tests
  (define adder (make-adder 5))
  (adder 8)
  ; expect 13
;

;; Extra questions

(define lst
  (cons (cons 1 nil) (cons 2 (cons '(3 4) '(5))))
)

(define (composed f g)
  ; Returns a new procedure which takes in a number x and returns the result of calling f on g of x.
  (lambda (x) (f (g x)))
)

(define (remove item lst)
  ; Returns a new list with all instances of item removed from list lst. Assume no nested lists and only number elements.
  (filter-lst (lambda (x) (not (= x item))) lst)
)

;;; Tests
  (remove 3 nil)
  ; expect ()
  (remove 3 '(1 3 5))
  ; expect (1 5)
  (remove 5 '(5 3 5 5 1 4 5 4))
  ; expect (3 1 4 4)
;

(define (no-repeats s)
  ; Returns a list that has all of the unique elements of list s in the order that they first appear.
  ; Same as unique function from HW06
  (if (null? s)
    nil
    (cons (car s) (no-repeats (filter-lst (lambda (x) (not (= (car s) x))) (cdr s)))))
)

(define (substitute s old new)
  ; Returns a list with the elements of s, but with every occurence of old replaced by new, even within sub-lists.
  (cond ((null? s) nil)
        ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
        ((equal? (car s) old) (cons new (substitute (cdr s) old new)))
        (else (cons (car s) (substitute (cdr s) old new))))

)

;;; Tests
  (substitute '(1 a 3 (a 3 (4 5 a)) a b a) 'a 2)
  ; expect (1 2 3 (2 3 (4 5 2)) 2 b 2)
;

(define (sub-all s olds news)
  ; Returns a list with the elements of s, but with each word that occurs in the list olds replaced by the corresponding word of list news.
  ; olds and news are of same length and have no elements in common.
  (if (or (null? s) (null? olds)) s
        (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
    )
)