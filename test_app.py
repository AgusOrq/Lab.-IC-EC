from app import saludo, app

def test_saludo():
    assert saludo("mundo") == "Hola, mundo!"

def test_home():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "Hola, mundo!" in respuesta.get_data(as_text=True)