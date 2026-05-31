from app import saludo, app

def test_saludo():
    assert saludo("mundo").startswith("Hola,")

def test_home():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "Hola," in respuesta.get_data(as_text=True)

# Prueba para demostrar el gate del pipeline
def test_fallo_intencional():
    assert saludo("mundo") == "Esto nunca coincide"