from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    dataAtual = datetime.datetime.now()
    newYear = dataAtual.month == 1 and dataAtual.day == 1

    return render_template("index.html", newYear=newYear)