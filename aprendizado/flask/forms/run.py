from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
# O tipo de solicitação que a rota "/" aceita é somente do método POST
def hello():
    if request.method == "GET":
        return "Por favor, submeta seu nome no formulário"
    else:
        name = request.form.get("identificação")
        return render_template("hello.html", name=name)