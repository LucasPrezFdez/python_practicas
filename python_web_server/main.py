from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def home():
    return "Bienvenido a mi servidor Python con Flask"


@app.route("/suma")
def suma():
    a = request.args.get("a")
    b = request.args.get("b")
    resultado = a + b
    return f"La suma es {resultado}"


@app.route("/saluda")
def saluda():
    return "Hola!!!!"


# arranca el servidor (demonio / servicio)
# puerto por defecto (5000?)

if __name__ == "__main__":
    app.run()
