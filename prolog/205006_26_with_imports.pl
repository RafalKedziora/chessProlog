:- [facts_full].
% :- [facts_limited]. -- odkomentować tę linię i zakomentować powyższą dla ograniczonego zakresu predykatów

clues(S) :- 
  valid(_, S), % zakomentować dla ograniczonego zakresu predykatów
  f4(piece(king, one, white), S), % Biały król znajduje się na polu F4.
  edge(piece(bishop, _, black), S), % Czarny goniec znajduje się przy krawędzi szachownicy.
  king_attacks(piece(king, one, white), piece(rook, one, black), S), % Biały król może bić pierwszą wieżę.
  knight_attacks(piece(knight, one, black), piece(pawn, two, white), S), % Pierwszy czarny skoczek może bić drugiego pionka.
  king_attacks(piece(king, one, black), piece(bishop, one, white), S), % Czarny król może bić pierwszego gońca.
  black_pawn_attacks(piece(pawn, one, black), piece(bishop, one, white), S), % Pierwszy czarny pionek może bić pierwszego gońca.
  white_pawn_attacks(piece(pawn, one, white), piece(knight, one, black), S), % Pierwszy biały pionek może bić pierwszego skoczka.
  knight_attacks(piece(knight, one, black), piece(king, one, white), S), % Pierwszy czarny skoczek może bić króla.
  rook_attacks(piece(rook, one, white), piece(knight, one, black), S), % Pierwsza biała wieża może bić pierwszego skoczka.
  bishop_attacks(piece(bishop, one, white), piece(pawn, one, black), S), % Pierwszy biały goniec może bić pierwszego pionka.
  king_attacks(piece(king, one, white), piece(pawn, two, black), S), %  Biały król może bić drugiego pionka
  knight_attacks(piece(knight, one, black), piece(pawn, three, white), S), % Pierwszy czarny skoczek może bić trzeciego pionka.
  knight_attacks(piece(knight, one, black), piece(bishop, two, white), S), % Pierwszy czarny skoczek może bić drugiego gońca.
  bishop_attacks(piece(bishop, two, black), piece(king, one, white), S), % Drugi czarny goniec może bić króla.
  rook_attacks(piece(rook, one, black), piece(pawn, three, white), S), % Pierwsza czarna wieża może bić trzeciego pionka.
  rook_attacks(piece(rook, one, black), piece(king, one, white), S), % Pierwsza czarna wieża może bić króla.
  white_pawn_attacks(piece(pawn, one, white), piece(rook, one, black), S), % Pierwszy biały pionek może bić pierwszą wieżę.
  bishop_attacks(piece(bishop, two, black), piece(bishop, one, white), S), %  Drugi czarny goniec może bić pierwszego gońca.
  black_pawn_attacks(piece(pawn, one, black), piece(pawn, three, white), S), % Pierwszy czarny pionek może bić trzeciego pionka.
  rook_attacks(piece(bishop, two, white), piece(king, one, black), S), % Gdyby drugi biały goniec był wieżą mógłby bić czarnego króla.
  bishop_attacks(piece(bishop, two, black), piece(bishop, two, white), S), % mirror | Drugi czarny goniec może bić drugiego gońca.
  bishop_attacks(piece(bishop, two, black), piece(pawn, three, white), S), % Drugi czarny goniec może bić trzeci pionek.
  bishop_attacks(piece(bishop, one, black), piece(queen, one, white), S), %  Pierwszy czarny goniec może bić hetmana.
  black_pawn_attacks(piece(pawn, two, black), piece(king, one, white), S), % Drugi czarny pionek może bić króla.
  bishop_attacks(piece(bishop, two, white), piece(bishop, two, black), S), % mirror | Drugi biały goniec może bić drugiego gońca.
  white_pawn_attacks(piece(pawn, three, white), piece(pawn, one, black), S), % Trzeci biały pionek może bić pierwszego pionka.
  king_attacks(piece(king, one, black), piece(rook, one, white), S), %  Czarny król może bić pierwszą wieżę.
  king_attacks(piece(king, one, white), piece(bishop, two, black), S). % Biały król może bić drugiego gońca.