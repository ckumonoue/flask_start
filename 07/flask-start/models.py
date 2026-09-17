from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Kategoria(db.Model):  # 9
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(50), nullable=False, unique=True)
    ksiazki = db.relationship('Ksiazka', backref='kategoria', lazy=True)

    def __repr__(self):
        return f"<Kategoria {self.nazwa}>"

class Ksiazka(db.Model):  # 1
    id = db.Column(db.Integer, primary_key=True)
    tytul = db.Column(db.String(150), nullable=False)
    cena = db.Column(db.Float, nullable=False)
    dostepna = db.Column(db.Boolean, default=True)
    rok_wydania = db.Column(db.Integer, nullable=True)
    kategoria_id = db.Column(db.Integer, db.ForeignKey('kategoria.id'), nullable=True)  # 9

    def __repr__(self):
        return f"<Ksiazka {self.tytul}>"

    def wiek_ksiazki(self):  # 7
        if self.rok_wydania:
            return datetime.date.today().year - self.rok_wydania
        return None

    def cena_brutto(self):
        return round(self.cena * 1.05, 2)  # VAT 5% 