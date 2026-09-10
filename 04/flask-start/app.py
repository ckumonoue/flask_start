from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
 return "Mykyta"
@app.route("/ogloszenie/dodaj")
def dodaj():
 return "Dodaje nowe ogloszenie"
@app.route("/ogloszenie/usun")
def usun():
 return "Usuwam ogloszenie"
@app.route("/szukaj")
def szukaj():
 return "Szukam ogloszenie"
@app.route("/admin")
def admin():
 return "Brak dostepu", 403
@app.route("/api/info")
def status():
 return {"portal": True, "autor": "Mykyta", "wersja": "0.1"}
if __name__ == "__main__":
 app.run(debug=True)