from flask import Flask, render_template, request, redirect, url_for
from models import db, Ksiazka, Kategoria

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ksiegarnia.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def lista():  # 3 / 6
    q = request.args.get("q")
    tylko_dostepne = request.args.get("tylko_dostepne")

    query = Ksiazka.query

    if tylko_dostepne == "1":
        query = query.filter_by(dostepna=True)
    if q:
        query = query.filter(Ksiazka.tytul.contains(q))

    ksiazki = query.order_by(Ksiazka.tytul).all()
    return render_template("lista.html", ksiazki=ksiazki)

@app.route("/ksiazka/<int:id>")
def szczegoly(id):  # 3
    k = Ksiazka.query.get_or_404(id)
    return render_template("szczegoly.html", k=k)

@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():  # 4
    if request.method == "POST":
        tytul = request.form["tytul"]
        cena = float(request.form["cena"])
        dostepna = "dostepna" in request.form
        rok_wydania = int(request.form["rok_wydania"]) if request.form.get("rok_wydania") else None
        kategoria_id = int(request.form["kategoria_id"]) if request.form.get("kategoria_id") else None

        nowa = Ksiazka(
            tytul=tytul,
            cena=cena,
            dostepna=dostepna,
            rok_wydania=rok_wydania,
            kategoria_id=kategoria_id
        )
        db.session.add(nowa)
        db.session.commit()
        return redirect(url_for("lista"))
    
    kategorie = Kategoria.query.all()
    return render_template("dodaj.html", kategorie=kategorie)

@app.route("/edytuj/<int:id>", methods=["GET", "POST"])
def edytuj(id):  # 5
    k = Ksiazka.query.get_or_404(id)
    if request.method == "POST":
        k.tytul = request.form["tytul"]
        k.cena = float(request.form["cena"])
        k.dostepna = "dostepna" in request.form
        k.rok_wydania = int(request.form["rok_wydania"]) if request.form.get("rok_wydania") else None
        k.kategoria_id = int(request.form["kategoria_id"]) if request.form.get("kategoria_id") else None

        db.session.commit()
        return redirect(url_for("szczegoly", id=k.id))

    kategorie = Kategoria.query.all()
    return render_template("edytuj.html", k=k, kategorie=kategorie)

@app.route("/usun/<int:id>", methods=["POST"])
def usun(id):  # 4
    k = Ksiazka.query.get_or_404(id)
    db.session.delete(k)
    db.session.commit()
    return redirect(url_for("lista"))

if __name__ == "__main__":
    app.run(debug=True)