# Notatki: HTTP

## Kody odpowiedzi

| Kod | Nazwa        | Gdzie                                       |
|-----|--------------|---------------------------------------------|
| 200 | OK           | udane otwarcie `/products`                  |
| 302 | Found        | przekierowanie po dodaniu produktu          |
| 404 | Not Found    | `/products/999` – produkt nie istnieje      |
| 405 | Method Not Allowed | `GET` na trasie tylko z `POST` (delete) |
| 500 | Internal Server Error | błąd w kodzie widoku               |

## Metody HTTP

- `GET` – pobiera zasób, nie zmienia danych na serwerze.
- `POST` – wysyła dane do serwera, np. formularz dodawania produktu.
- `PUT` – zastępuje cały zasób nowymi danymi.
- `PATCH` – zmienia część zasobu.
- `DELETE` – usuwa zasób.

## Przykład: abort(404)

```python
from flask import abort

@app.route("/products/<int:id>")
def product_detail(id):
    product = db.session.get(Product, id)
    if product is None:
        abort(404)
    return render_template("products/detail.html", product=product)
```

> Uwaga: formularze HTML obsługują tylko `GET` i `POST`, dlatego usuwanie robimy przez `POST`.
