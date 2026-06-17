from flask import Flask, render_template, request, redirect, url_for, flash, session
from backend import db
import uuid

app = Flask(__name__)
app.secret_key = "secret123"


# ---------------- LOGIN ---------------- #

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        users = db.collection("users").where("email","==",email).stream()

        for user in users:
            data = user.to_dict()

            if data["password"] == password:

                session["user"] = email
                flash("Login Successful")

                return redirect(url_for("home"))

        flash("Invalid Email or Password")

    return render_template("login.html")


# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        db.collection("users").add({
            "name": name,
            "email": email,
            "password": password
        })

        flash("Registration Successful")

        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.pop("user", None)

    flash("Logged out successfully")

    return redirect(url_for("login"))


# ---------------- HOME ---------------- #

@app.route("/home")
def home():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("home.html")

@app.route("/menu")
def menu():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("menu.html")

# ---------------- MENUS ---------------- #

@app.route("/vegfoodmenu")
def vegfoodmenu():
    return render_template("vegFoodMenu.html")


@app.route("/nonvegmenu")
def nonvegmenu():
    return render_template("nonVegMenu.html")


@app.route("/nonvegstarter")
def nonvegstarter():
    return render_template("NonVegStarters.html")


@app.route("/vegstarter")
def vegstarter():
    return render_template("VegStarters.html")


@app.route("/desserts")
def desserts():
    return render_template("DESSERTS.html")


@app.route("/mocktails")
def mocktails():
    return render_template("Moctails.html")


@app.route("/icecream")
def icecream():
    return render_template("IceCreme.html")


# ---------------- FOOD ITEMS ---------------- #

@app.route("/chickendummbiriyani")
def chickendummbiriyani():
    return render_template("PaymentOption.html", food="Chicken Dum Biryani", price=200)


@app.route("/muttondummbiriyani")
def muttondummbiriyani():
    return render_template("PaymentOption.html", food="Mutton Dum Biryani", price=400)


@app.route("/fishbiriyani")
def fishbiriyani():
    return render_template("PaymentOption.html", food="Fish Biryani", price=350)


@app.route("/prawnbiriyani")
def prawnbiriyani():
    return render_template("PaymentOption.html", food="Prawn Biryani", price=300)


@app.route("/chickenjointbiriyani")
def chickenjointbiriyani():
    return render_template("PaymentOption.html", food="Chicken Joint Biryani", price=250)


@app.route("/chickenboneless")
def chickenboneless():
    return render_template("PaymentOption.html", food="Chicken Boneless Biryani", price= 299)


@app.route("/chicken65")
def chicken65():
    return render_template("PaymentOption.html", food="Chicken 65", price= 249)


@app.route("/chickengheeroast")
def chickengheeroast():
    return render_template("PaymentOption.html", food="Chicken Ghee Roast", price= 400)


@app.route("/cashewpalao")
def cashewpalao():
    return render_template("PaymentOption.html", food="Cashew Pulao", price= 199)


@app.route("/cholebattore")
def cholebattore():
    return render_template("PaymentOption.html", food="Chole Battore", price= 249)


@app.route("/mushroombiriyani")
def mushroombiriyani():
    return render_template("PaymentOption.html", food="Mushroom Biryani", price= 350)


@app.route("/paneerbiriyani")
def paneerbiriyani():
    return render_template("PaymentOption.html", food="Paneer Biryani", price= 200)


@app.route("/shahipaneer")
def shahipaneer():
    return render_template("PaymentOption.html", food="Shahi Paneer", price= 230)


@app.route("/butternaan")
def butternaan():
    return render_template("PaymentOption.html", food="Butter Naan", price= 40)


@app.route("/tomatorice")
def tomatorice():
    return render_template("PaymentOption.html", food="Tomato Rice", price= 149)


@app.route("/vegetablepulao")
def vegetablepulao():
    return render_template("PaymentOption.html", food="Vegetable Pulao", price= 149)


# ---------------- STARTERS ---------------- #

@app.route("/chickenlollipop")
def chickenlollipop():
    return render_template("PaymentOption.html", food="Chicken Lollipop", price= 199)


@app.route("/chickentikka")
def chickentikka():
    return render_template("PaymentOption.html", food="Chicken Tikka", price= 249)


@app.route("/fishtikka")
def fishtikka():
    return render_template("PaymentOption.html", food="Fish Tikka", price= 350)


@app.route("/garlicprawn")
def garlicprawn():
    return render_template("PaymentOption.html", food="Garlic Prawn", price= 200)


@app.route("/muttonribfry")
def muttonribfry():
    return render_template("PaymentOption.html", food="Mutton Rib Fry", price= 230)


@app.route("/alootikka")
def alootikka():
    return render_template("PaymentOption.html", food="Aloo Tikka", price= 199)


# ---------------- DESSERTS ---------------- #

@app.route("/doublekamitta")
def doublekamitta():
    return render_template("PaymentOption.html", food="Double Ka Meetha", price= 249)


@app.route("/momos")
def momos():
    return render_template("PaymentOption.html", food="Momos", price= 350)


@app.route("/paneertikka")
def paneertikka():
    return render_template("PaymentOption.html", food="Paneer Tikka", price= 200)


@app.route("/vegrolls")
def vegrolls():
    return render_template("PaymentOption.html", food="Veg Rolls", price= 230)


@app.route("/samosas")
def samosas():
    return render_template("PaymentOption.html", food="Samosas", price= 230)


@app.route("/cookies")
def cookies():
    return render_template("PaymentOption.html", food="Cookies", price= 19)


@app.route("/cupcake")
def cupcake():
    return render_template("PaymentOption.html", food="Cup Cake", price= 49)


@app.route("/pastries")
def pastries():
    return render_template("PaymentOption.html", food="Pastries", price= 35)


# ---------------- MOCKTAILS ---------------- #

@app.route("/dragonfruit")
def dragonfruit():
    return render_template("PaymentOption.html", food="Dragon Fruit Mocktail", price= 250)


@app.route("/orange")
def orange():
    return render_template("PaymentOption.html", food="Orange Mocktail", price= 200)


@app.route("/strawberry")
def strawberry():
    return render_template("PaymentOption.html", food="Strawberry Mocktail", price= 260)


@app.route("/roseapple")
def roseapple():
    return render_template("PaymentOption.html", food="Rose Apple Mocktail", price= 300)


@app.route("/blueberry")
def blueberry():
    return render_template("PaymentOption.html", food="Blueberry Mocktail", price= 330)


# ---------------- ICE CREAM ---------------- #

@app.route("/chocolate")
def chocolate():
    return render_template("PaymentOption.html", food="Chocolate Ice Cream", price= 125)


@app.route("/orangeIce")
def orangeIce():
    return render_template("PaymentOption.html", food="orange Ice Cream", price= 100)
                           
@app.route("/strawberryIce")
def strawberryIce():
    return render_template("PaymentOption.html", food="strawberry Ice Cream", price= 120)

@app.route("/pista")
def pista():
    return render_template("PaymentOption.html", food="Pista Ice Cream", price= 150)


@app.route("/venella")
def venella():
    return render_template("PaymentOption.html", food="Vanilla Ice Cream", price= 90)


# ---------------- PLACE ORDER ---------------- #

@app.route("/placeorder", methods=["POST"])
def placeorder():

    if "user" not in session:
        return redirect(url_for("login"))

    food = request.form["food"]
    price = int(request.form["price"])
    qty = int(request.form["qty"])

    total = price * qty

    order_id = str(uuid.uuid4())[:8]

    db.collection("orders").add({

        "order_id": order_id,
        "user": session["user"],
        "food": food,
        "price": price,
        "quantity": qty,
        "total": total

    })

    return render_template("paymentdone.html",
                           order_id=order_id,
                           food=food,
                           qty=qty,
                           total=total)



# ---------------- MY ORDERS ---------------- #

@app.route("/myorders")
def myorders():

    if "user" not in session:
        return redirect(url_for("login"))

    orders = db.collection("orders").where("user","==",session["user"]).stream()

    order_list = []

    for order in orders:
        order_list.append(order.to_dict())

    return render_template("myorders.html", orders=order_list)


# ---------------- USER PROFILE ---------------- #

@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect(url_for("login"))

    users = db.collection("users").where("email","==",session["user"]).stream()

    for user in users:
        data = user.to_dict()

    return render_template("profile.html", user=data)



# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    app.run(debug=True)