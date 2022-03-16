from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/home")
def home():
    return redirect(url_for("index"))


@app.route("/shop")
def shop():
    return render_template("shop.html", title="Shop")
