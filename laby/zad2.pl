parent(janina, anna).
parent(edward, anna).
parent(marian, andrzej).
parent(wilhemina, andrzej).
parent(andrzej, magdalena).
parent(tomasz, magdalena).
parent(andrzej, tomasz).
parent(anna, tomasz).
parent(tomasz, zuzanna).
parent(karolina, zuzanna).

male(edward).
male(marian).
male(andrzej).
male(tomasz).

female(janina).
female(anna).
female(magdalena).
female(wilhemina).
female(karolina).
female(zuzanna).

son(X, Y) :- parent(Y, X), male(X).
granddaughter(X, Y) :- parent(Y, Z), parent(Z, X), female(X).
partner(X, Y) :- parent(X, Z) , parent(Y, Z),  X \= Y.
aunt(X, Y) :- parent(Z, W), parent(W, Y), parent(Z, X).