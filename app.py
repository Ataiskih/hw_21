from flask import Flask, render_template


app = Flask(__name__)
@app.route("/") # маршрутизатор
def homepage():
    return "<h1>Welcome to furniture shop!</h1>"

@app.route("/types")
def types_of_furniture():
    return render_template("types.html")

@app.route("/kitchen")
def kitchen_furniture():
    return render_template("kitchen.html")

@app.route("/special/<name>")
def special_offer(name):
    name = name.capitalize()# делает первую букву заглавную
    return render_template("special.html", name = name)
