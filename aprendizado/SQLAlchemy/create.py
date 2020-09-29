from flask import Flask, render_template, request
from models import *
# importando as classes do arquivo models.py

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# estas configurações estão dizendo ao nosso aplicativo Flask qual banco de dados usar

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
# vincule o banco de dados (db) com a aplicação Flask (app)

def main():
    db.create_all()
    # criará as tabelas em nosso banco de dados de acordo com cada classe definida

if __name__ == "__main__":
    with app.app_context():
        main()
# precisa disso para rodar perfeitamente

