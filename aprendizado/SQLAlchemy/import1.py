import csv
import os

from flask import Flask, render_template, request
from models import * 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# estas configurações estão dizendo ao nosso aplicativo Flask qual banco de dados usar

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# como usar este banco de dados

db.init_app(app)
# vincule o banco de dados (db) com a aplicação Flask (app)

def main():
    f = open("flights.csv")
    reader = csv.reader(f)

    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)

        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()