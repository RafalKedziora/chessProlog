member1(H, [H|T]).
member1(H,[_|T]):- member1(H,T).

% concat = append
concat1([], L2, L2).
concat1([H|T], X, [H|Y]):- concat1(T, X, Y).

delete1(X,[X|Tail],Tail).
delete1(X,[H|Old],[H|New]):- delete1(X,Old,New).

len([] , 0 ).
len([_|X] , L ):- len(X,N) , L is N+1 .

rlen([Head|Tail],N):-rlen(Head,Q1),rlen(Tail,Q2),!,N is Q1+Q2.
rlen([],0):-!.
rlen(X,1):-!.

reverse1([],[]).
reverse1([Head|Tail],L2):-reverse(Tail, L1), concat1(L1,[Head],L2).
reverse2([Head|Tail],Accumulator,L3):-reverse2(Tail,[Head|Accumulator],L3).
reverse2([],Accumulator,Accumulator).

sum([], 0).
sum([X|XS], N):- sum(XS, M), N is M + X.

avg(L,N):-sum(L,Q),len(L,W),N is Q/W.

count(X, [], 0).
count(X, [X|T], N):- count(X,T,M), N is M+1.
count(X, [_|T], N):- count(X,T,N).

double([], []).
double([X|Y], [X,X|Z]):- double(Y,Z).

repeat([], [], N):-!.
repeat([H1|T1], L2, N) :- repeat(T1, L3, N), rep(H1, L4, N), concat1(L4, L3, L2).

rep(X,[],0) :- !. 
rep(Head,[Head|Tail],N) :- Q is N - 1, rep(Head, Tail, Q).
