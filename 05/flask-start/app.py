from flask import Flask, request, redirect, url_for, abort
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello world!!!!"

#1
@app.route("/czesc/<imie>")
def czesc_imie(imie):
    return f"Cześć, {imie}!"

@app.route("/czesc/<imie>/<int:wiek>")
def czesc_wiek(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat"

#2
@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"{a} * {b} = {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"

@app.route("/potega/<int:a>/<int:b>")
def potega(a, b):
    return f"{a} ^ {b} = {a ** b}"

# 3
@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if n < 1 or n > 20:
        return "Przekroczono zakres (dozwolony: 1-20)", 400
    wiersze = [f"{n} x {i} = {n * i}" for i in range(1, 11)]
    return "<br>".join(wiersze)

# 4
@app.route("/produkty")
def produkty():
    kat = request.args.get("kat", "wszystkie")
    sort = request.args.get("sort", "domyślne")
    return f"Kategoria: {kat}, sortowanie: {sort}"

# 5
sale = {
    1: "W109",
    2: "W104",
    3: "305",
    4: "102",
    5: "W111"
}

@app.route("/element/<int:id>")
def element(id):
    if id not in sale:
        abort(404)
    return f"Sala: {sale[id]}"

@app.route("/elementy")
def elementy():
    return "<br>".join(f"{id}: {nazwa}" for id, nazwa in sale.items())


# 6
@app.route("/start")
def start():
    return redirect(url_for("main"))

if __name__ == "__main__":
 app.run(debug=True)