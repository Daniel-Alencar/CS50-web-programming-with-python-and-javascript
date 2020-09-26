from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/<string:name>")
def helloName(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1><p>loremakbch fgaskgcfnsgfmbhfnk sangn shgdnfn sh fsmdfb sdhfmshfsgv gsjkfgb ,fg dmhfg dhfgb shbf kusgb skugb kfn ukgbskgbksgb sskgb hskgksbskghskg sigsiduk gbdskg s</p>"