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
    flights = Flight.query.all()
    # flifhts é uma lista de objetos, neste caso, uma lista de Flights (voos), o qual pode ser acessado cada propriedade de um objeto em específico usando:
    # flight.origin
    # flight.destination
    # flight.duration
    
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} -- {flight.duration} minutes.")



if __name__ == "__main__":
    with app.app_context():
        main()

