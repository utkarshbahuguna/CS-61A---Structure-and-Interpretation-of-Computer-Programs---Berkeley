; https://inst.eecs.berkeley.edu/~cs61a/fa19/hw/hw08/

; List Comprehensions

; Implement a list-of macro which can be called as follows:
; (list-of <map-expression> for <name> in <list> if <conditional-expression>)

(define-macro (list-of map-expr for var in lst if filter-expr)
      `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

; if optional
(define-macro (list-of map-expr-if-opeitonal for var in lst . condition)
      `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,(cond ((null? condition) #t) 
                                                                        ((eq? (car condition) 'if) (car (cdr condition))))) ,lst))
)