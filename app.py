from flask import Flask

app = Flask(__name__)

def saludo(nombre):
    return f"Hola, {nombre}!"

@app.route("/")
def home():
    return saludo("Profe Minoli")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)