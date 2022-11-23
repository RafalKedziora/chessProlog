isnumber(zero).
isnumber(s(X)) :- isnumber(X). 

isequal(X,X) :- isnumber(X).
isequal(s(X),s(Y)) :- isequal(X,Y).

lessthanequal(zero,X) :- isnumber(X).
lessthanequal(s(X),s(Y)) :- lessthanequal(X,Y).

add(zero,X,X) :- isnumber(X).
add(s(X),Y,s(Z)) :- add(X,Y,Z).

even(zero).
even(s(X)) :- odd(X). 
odd(s(X)) :- even(X). 

times(zero, X, zero) :- isnumber(X).
times(s(X), Y, Z) :- times(X, Y, Q), add(Y, Q, Z).

quotient(_, zero, _) :- false.
quotient(X, Y, Q) :- times(Y, Q, X).

remainder(X, Y, R) :- lessthanequal(X,Y), R = X.
remainder(zero, _, zero).
remainder(_, zero, _) :- false.
remainder(X, Y, R) :- add(Y, Q, X), remainder(Q, Y, R).

fact(zero, s(zero)).
fact(s(N), X) :- fact(N, A), times(A, s(N), X).

fibonacci(zero, zero).
fibonacci(s(zero), s(zero)).
fibonacci(s(s(zero)), s(zero)).
fibonacci(s(s(N)), X) :- fibonacci(s(N), A), fibonacci(N, B), add(A, B, X).

% do testowania

shownum(zero,0).
shownum(s(X),Y) :- shownum(X,Q), Y is Q + 1.

putnum(zero,0).
putnum(s(X),Y) :- Q is Y - 1, putnum(X,Q).
