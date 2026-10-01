# Sklep Internetowy (Flask)

Aplikacja internetowa napisana w języku Python z użyciem frameworka Flask i ORM SQLAlchemy, dostosowana do standardów PEP 8 oraz zasad czystego kodu.

---

## Instrukcja uruchomienia

1. **Stwórz i aktywuj środowisko wirtualne:**

   ```bash
   python -m venv venv

   # Windows (PowerShell / CMD):
   venv\Scripts\activate

   # Linux / macOS:
   source venv/bin/activate
   ```

2. **Zainstaluj wymagane pakiety:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Uruchom aplikację:**

   ```bash
   python app.py
   ```

---

## Struktura projektu

```text
├── app.py           # Konfiguracja i widoki aplikacji (kontrolery)
├── models.py        # Modele bazy danych SQLAlchemy
├── templates/       # Szablony Jinja2 (HTML)
├── static/          # Pliki statyczne (CSS, JS)
├── requirements.txt # Zależności projektu
└── README.md        # Dokumentacja projektu
```

---

## Tabela tras (Endpoints)

| Metoda | Adres | Opis | Możliwe kody odpowiedzi |
| :--- | :--- | :--- | :--- |
| **GET** | `/products` | Lista wszystkich produktów | `200 OK` |
| **GET** | `/products/<int:product_id>` | Szczegóły konkretnego produktu | `200 OK`, `404 Not Found` |
| **GET / POST** | `/products/add` | Wyświetlanie formularza (`GET`) oraz dodawanie produktu (`POST`) | `200 OK`, `302 Found` |
| **GET / POST** | `/products/<int:product_id>/edit` | Wyświetlanie formularza edycji (`GET`) i zapis zmian (`POST`) | `200 OK`, `302 Found`, `404 Not Found` |
| **POST** | `/products/<int:product_id>/delete` | Usuwanie produktu z bazy danych | `302 Found`, `404 Not Found` |

---

## Testy kodów odpowiedzi HTTP

| Adres | Metoda | Kod | Opis / Sytuacja testowa |
| :--- | :--- | :--- | :--- |
| `/products` | `GET` | `200 OK` | Udane pobranie listy produktów. |
| `/products/add` | `POST` | `302 Found` | Udane dodanie nowego produktu – przekierowanie (redirect) na listę. |
| `/products/999` | `GET` | `404 Not Found` | Żądanie produktu, którego nie ma w bazie (`get_or_404`). |
| `/products/1/delete` | `GET` | `405 Method Not Allowed` | Wywołanie trasy usuwania metodą `GET` zamiast `POST`. |
| `/products/add` | `POST` | `400 Bad Request` | Przesłanie niepoprawnych danych w formularzu (np. litery w cenie). |
| `/test-error` | `GET` | `500 Internal Server Error` | Celowe wywołanie wyjątku w kodzie w celach testowych. |

---

## Standardy, Jakość Kodu i Bezpieczeństwo

### Bezpieczny GET
Metoda `GET` jest bezpieczna i idempotentna – służy wyłącznie do pobierania danych. W całej aplikacji żaden kod wywoływany metodą `GET` nie zmienia stanu bazy danych, co chroni aplikację przed przypadkowym usunięciem lub modyfikacją danych przez boty oraz mechanizmy *prefetch* przeglądarek.

### Raport narzędzia Ruff
Po instalacji narzędzia `ruff` i uruchomieniu komendy `ruff check .` wykryto 4 problemy:
- **F401:** Nieużywany import `import os` w pliku `app.py`.
- **E302:** Brak 2 pustych linii przed definicją klasy w `models.py`.
- **E501:** Linia przekraczająca standardową długość znaków.
- **W292:** Brak pustej linii na końcu pliku.

Wszystkie błędy zostały automatycznie naprawione poleceniem `ruff check . --fix`, a kod został sformatowany przy użyciu `ruff format .`.

### Dokumentacja kodu i Type Hints
Każdy moduł, klasa oraz funkcja widoku posiadają docstringi zgodne ze standardem **PEP 257**. Funkcje zawierają również adnotacje typów (*type hints*).

Przykład wyniku wywołania `help(Product)` w `flask shell`:

```text
Help on class Product in module models:

class Product(flask_sqlalchemy.model.Model)
 |  Produkt w sklepie.
 |  
 |  Cena przechowywana jako netto; brutto liczy gross_price().
 |  Produkt niedostępny (is_available=False) nie znika z bazy,
 |  tylko nie pokazuje się na liście.
 |  
 |  Methods defined here:
 |  
 |  gross_price(self) -> float
 |      Zwraca cenę brutto (netto + 23% VAT), zaokrągloną do groszy.
```

---

## Definition of Done (Checklista)

- [x] Aplikacja uruchamia się z czystego klonu: `pip install -r requirements.txt`, `python app.py`
- [x] Nazwy zmiennych, funkcji, klas, tras – po angielsku, zgodnie z PEP 8
- [x] `ruff check .` nie zgłasza błędów, `ruff format .` nic nie zmienia
- [x] Każda funkcja widoku i każdy model ma docstring
- [x] Nowe funkcje mają type hints
- [x] Żaden `GET` nie zmienia danych (usuwanie, dodawanie = `POST`)
- [x] Po każdym `POST` następuje przekierowanie (`redirect`)
- [x] Nieistniejący zasób zwraca `404`, złe dane `400` – nie `500`
- [x] Plik `.gitignore` obejmuje `venv/`, `instance/`, `*.db`, `__pycache__/`, `.env`
- [x] README zawiera: opis, instrukcję uruchomienia, strukturę oraz tabelę tras
- [x] Commity są małe, po angielsku i zgodne z przyjętą konwencją
- [x] Potrafisz wyjaśnić każdą linię kodu – także tę napisaną przez LLM