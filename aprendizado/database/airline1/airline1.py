import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight"""

    # get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
        # tente converter para um inteiro a informação pega do form (formulário)
    except ValueError:
        return render_template("error.html", message="Error! Invalid flight number")

    # make sure the flight exists
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        # rowcount nos trás uma contagem de linhas do que for retornado
        return render_template("error.html", message="No such flight with that id")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
                {"name": name, "flight_id": flight_id})
                # fazer isto evita as race conditions (colocar valores diretamente no SQL podendo realizar comandos)
    db.commit()
    return render_template("success.html", message="You have successfuly booked your flight")

@app.route("/flights")
def flights():
    """List all flights"""
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """Lists details about a single flight"""

    # make sure the flight exists
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flight with that id")

    # get all passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id", {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)
