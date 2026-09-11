from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# 1
@app.route("/")
def index():
    return render_template("index.html", projekt_nazwa="Steam", imie="Mykyta")

# 2
ELEMENTY = [
    {"id": 1, "nazwa": "GTA 6", "gatunek": "OAA", "cena": 399.99, "dostepny": False},
    {"id": 2, "nazwa": "Valorant", "gatunek": "FPS", "cena": 00.02, "dostepny": True},
    {"id": 3, "nazwa": "GTA:SA", "gatunek": "OAA", "cena": 69.99, "dostepny": False},
    {"id": 4, "nazwa": "Dota 2", "gatunek": "Strategia", "cena": 00.01, "dostepny": True},
    {"id": 5, "nazwa": "Minecraft", "gatunek": "Sandbox", "cena": 89.99, "dostepny": True},
]

# 2 / 5
@app.route("/lista")
def lista():
    return render_template("lista.html", elementy=ELEMENTY)

# 3
@app.route("/element/<int:id>")
def szczegoly(id):
    element = next((item for item in ELEMENTY if item["id"] == id), None)
    if element is None:
        abort(404)
    return render_template("szczegoly.html", element=element)

# 6
@app.route("/szukaj")
def szukaj():
    q = request.args.get("q", "").strip()
    wyniki = [e for e in ELEMENTY if q.lower() in e["nazwa"].lower()] if q else []
    return render_template("szukaj.html", q=q, wyniki=wyniki)

# 7
@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        nowy_element = {
            "id": len(ELEMENTY) + 1,
            "nazwa": request.form["nazwa"],
            "gatunek": request.form["gatunek"],
            "cena": float(request.form["cena"]),
            "dostepny": "dostepny" in request.form
        }
        ELEMENTY.append(nowy_element)
        return redirect(url_for("lista"))
    return render_template("dodaj.html")

if __name__ == "__main__":
    app.run(debug=True)