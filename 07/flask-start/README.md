# Projekt Flask - Księgarnia

## Struktura projektu MVC

| Warstwa MVC | Plik / Folder | Opis |
| :--- | :--- | :--- |
| **Model** | `models.py` | Klasy `Ksiazka` i `Kategoria` oraz logika biznesowa (metoda `wiek_ksiazki()`) |
| **View** | `templates/*.html` | Szablony HTML renderingujące dane |
| **Controller** | `app.py` | Trasy `@app.route`, pobieranie danych i przekierowania |

## Test CRUD (konsola `flask shell`)

```python
>>> from models import db, Ksiazka, Kategoria
>>> kat = Kategoria(nazwa="Fantastyka")
>>> db.session.add(kat)
>>> db.session.commit()

# CREATE (Dodanie 3 obiektów)
>>> k1 = Ksiazka(tytul="Wiedźmin", cena=49.99, dostepna=True, rok_wydania=1993, kategoria_id=kat.id)
>>> k2 = Ksiazka(tytul="Hobbit", cena=39.50, dostepna=True, rok_wydania=1937, kategoria_id=kat.id)
>>> k3 = Ksiazka(tytul="Stary wycofany podręcznik", cena=10.00, dostepna=False, rok_wydania=2000)
>>> db.session.add_all([k1, k2, k3])
>>> db.session.commit()

# READ (Wypisanie wszystkich)
>>> Ksiazka.query.all()
[<Ksiazka Wiedźmin>, <Ksiazka Hobbit>, <Ksiazka Stary podręcznik wycofany>]

# UPDATE (Edycja pola)
>>> k = Ksiazka.query.filter_by(tytul="Hobbit").first()
>>> k.cena = 34.99
>>> db.session.commit()

# DELETE (Usuwanie)
>>> k_do_usuniecia = Ksiazka.query.get(3)
>>> db.session.delete(k_do_usuniecia)
>>> db.session.commit()

# Zrobiłem README za pomocą AI