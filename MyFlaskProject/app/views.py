from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


    

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")


@app.route("/404.html")
def error():
    return render_template("404.html")







