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

quotient(X, zero, Q) :- false.
quotient(X, Y, Q) :- times(Y, Q, X).

remainder(zero, X, zero).
remainder(X, zero, R) :- false.
remainder(s(X), s(Y), R) :- remainder(X, s(Y), A), isequal(A, Y).
remainder(s(X), Y, R) :- remainder(X, Y, A), add(A, s(zero), R).

fact(zero, s(zero)).
fact(s(N), X) :- fact(N, A), times(A, s(N), X).

fibonacci(zero, zero).
fibonacci(s(zero), s(zero)).
fibonacci(s(s(zero)), s(zero)).
fibonacci(s(s(N)), X) :- fibonacci(s(s(N)), A), fibonacci(s(s(N)), B), add(A, B, N).