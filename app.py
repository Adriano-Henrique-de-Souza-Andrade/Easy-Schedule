from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "amoguskindasus"
@app.route("/login")
def index():
	return render_template("index.html")

@app.route("/cadastro", methods=["POST", "GET"])
def greet():
	return render_template("cadastro.html")

@app.route("/Calendario", methods=["POST", "GET"])
def back():
	return render_template("Calendario.html")