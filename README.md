# Rozwiązanie zadania "Szachy", zestaw 26
Niniejsze repozytorium zawiera rozwiązanie zadania "Szachy" na przedmiot Sztuczna Integligencja prowadzony na Wydziale Zastosowań Informatyki i Matematyki SGGW.

## Autorzy
- **Rafał Kędziora** (nr alb. 205006)
- **Dawid Wijata** (nr alb. 200822)

## Pliki projektu

**Główne rozwiązanie projektu znajduje się pod ścieżką** `./prolog/205006_26_full_one_file.pl`.

Krótkie wyjaśnienie funkcjonalności pod ścieżkami:
- `labs` - zadania z laboratoriów
- `scripts` - skrypt generatora do zadania "Szachy"
  - `main.py` - plik uruchomieniowy generatora; można używać go w dwóch trybach - generującym wszystkie bicia oraz generującym tylko te niezbędne do uzykania wyniku
- `prolog` - folder z plikami wygenerowanymi przez generator
  - `205006_26_full_one_file.pl` - **główny plik z rozwiązaniem** - sklejka wygenerowanych faktów z predykatem `clues(S)`; zawiera wszystkie możliwe bicia dla figur z zestawu
  - `205006_26_limited_one_file.pl` - dodatkowy plik z rozwiązaniem - sklejka wygenerowanych faktów z predykatem `clues(S)`; zawiera wyłącznie bicia potrzebne do uzyskania wyniku dla Zestawu 26
  - `205006_26.pl` - plik z rozwiązaniem używający plików `facts_full.pl` i `facts_limited.pl` jako źródła faktów
  -  `facts_full.pl` - plik z zestawem faktów, zawiera wszystkie możliwe bicia figur na szachownicy
  -  `facts_limited.pl` - plik z zestawem faktów, zawiera tylko niezbędne bicia figur na szachownicy

Plik `205006_26.png` zawiera ułożenie figur z rozwiązania na szachownicy.

## Odpowiedzi na pytania odnośnie planszy
1. Czy takie ułożenie figur na szachownicy jest możliwe zgodnie z zasadami?

    Względem zasad gry w szachy jedyne zastrzeżenia budzi obecność obu białych gońców na czarnych polach. Jednak jest to możliwe, o ile goniec z pola B6, był promowanym pionem z pola D8, który potem przeszedł na B6. Pomimo tego, że jest to możliwe, to prawdopodobieństwo jest podobne jak dla wystąpienia gambitu sandomierskiego (bliskie zeru).

2. Który kolor jako następny wykonuje ruch?

    Żaden z graczy nie wykona już ruchu, gdyż biały król jest matowany przez czarnego skoczka, gońca oraz wieżę.