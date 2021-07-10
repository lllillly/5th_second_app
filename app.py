from flask import Flask, render_template

app = Flask(__name__)  # 폴더이름


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/intro")
def intro():
    return render_template("intro.html")


@app.route("/docs")
def docs():
    return render_template("docs.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/support")
def support():
    return render_template("support.html")


@app.route("/community")
def community():
    return render_template("community.html")


app.run(debug=True)
