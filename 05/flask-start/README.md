## Lista tras
* **Powitanie:**
  * `/czesc/Mykyta` -> Cześć, Mykyta!
  * `/czesc/Mykyta/19` -> Cześć, Mykyta, masz 19 lat

* **Kalkulator:**
  * `/dodaj/10/5` -> 10 + 5 = 15
  * `/odejmij/10/5` -> 10 - 5 = 5
  * `/pomnoz/4/5` -> 4 * 5 = 20
  * `/podziel/10/2` -> 10 / 2 = 5.0 (dla `/podziel/10/0` zwraca kod HTTP 400)
  * `/potega/2/3` -> 2 ^ 3 = 8

* **Tabliczka mnożenia:**
  * `/tabliczka/5` -> Wyświetla tabliczkę dla 5 od 1 do 10 (zakres n: 1-20)

* **Query string:**
  * `/produkty` -> Kategoria: wszystkie, sortowanie: domyślne
  * `/produkty?kat=gry&sort=cena` -> Kategoria: gry, sortowanie: cena

* **Mini-baza (Słownik):**
  * `/elementy` -> Lista wszystkich obiektów
  * `/element/1` -> Dane elementu o ID 1 (brak ID zwraca kod HTTP 404)

* **Przekierowanie:**
  * `/start` -> Przekierowuje na strone główną `/` (kod HTTP 302)