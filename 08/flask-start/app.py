from flask import Flask, redirect, render_template, request, url_for
from models import Product, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/products")
def product_list() -> str:
    """Wyświetla listę produktów.

    Returns:
        Wyrenderowany szablon HTML z listą produktów.
    """
    products = Product.query.order_by(Product.name).all()
    return render_template("products/list.html", products=products)


@app.route("/products/<int:product_id>")
def product_detail(product_id: int) -> str:
    """Wyświetla szczegóły konkretnego produktu.

    Args:
        product_id: Identyfikator produktu w bazie.

    Returns:
        Wyrenderowany szablon szczegółów produktu.

    Raises:
        404: Gdy produkt o podanym id nie istnieje.
    """
    product = Product.query.get_or_404(product_id)
    return render_template("products/detail.html", product=product)


@app.route("/products/add", methods=["GET", "POST"])
def product_add():
    """Dodawanie nowego produktu.

    GET – wyświetla pusty formularz dodawania.
    POST – zapisuje nowy produkt w bazie i przekierowuje na listę.

    Returns:
        Wyrenderowany formularz (GET) lub przekierowanie (POST).
    """
    if request.method == "POST":
        name = request.form.get("name")
        price = float(request.form.get("price", 0))
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for("product_list"))

    return render_template("products/add.html")


@app.route("/products/<int:product_id>/edit", methods=["GET", "POST"])
def product_edit(product_id: int):
    """Edycja produktu[cite: 11].

    GET – wyświetla formularz wypełniony aktualnymi danymi[cite: 11].
    POST – zapisuje zmiany i przekierowuje na szczegóły produktu[cite: 11].

    Args:
        product_id: id produktu w bazie[cite: 11].

    Returns:
        Wyrenderowany szablon (GET) lub redirect (POST)[cite: 11].

    Raises:
        404: gdy produkt o podanym id nie istnieje[cite: 11].
    """
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.name = request.form.get("name")
        product.price = float(request.form.get("price", 0))
        db.session.commit()
        return redirect(url_for("product_detail", product_id=product.id))

    return render_template("products/edit.html", product=product)


@app.route("/products/<int:product_id>/delete", methods=["POST"])
def product_delete(product_id: int):
    """Usuwa produkt z bazy danych.

    Wykonuje operację wyłącznie dla żądań POST[cite: 9, 10].

    Args:
        product_id: id produktu w bazie.

    Returns:
        Redirect na listę produktów.
    """
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("product_list"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)