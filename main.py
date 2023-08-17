from flask import Flask

APP = Flask(__name__)
APP.debug = False

@APP.route("/")
def index():
    return "<h1>Docker</h1>"

@APP.route("/ola")
def ola():
    return "<h1>Olá, mundo!</h1>"

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8180)
