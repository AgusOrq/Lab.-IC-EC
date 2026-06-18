# Especificación del proyecto

## 1. Intención
Aplicación web mínima que muestra un saludo. Sirve como ejemplo simple
para demostrar un entorno completo de integración y entrega continua.

## 2. Requisitos funcionales
- RF1: El sistema debe ofrecer una función que, dado un nombre, genere un saludo.
- RF2: El sistema debe exponer una página web en la ruta principal ("/")
  que muestre ese saludo.

## 3. Criterios de aceptación
Cada criterio es verificable mediante una prueba automatizada.
- CA1: La función de saludo devuelve un texto que comienza con "Hola,".
  (verificado por test_saludo)
- CA2: La ruta "/" responde con código HTTP 200.
  (verificado por test_home)
- CA3: La respuesta de la ruta "/" contiene un saludo con "Hola,".
  (verificado por test_home)

## 4. Restricciones técnicas
- Lenguaje: Python 3.12
- Framework web: Flask
- Servidor de producción: gunicorn
- Pruebas automatizadas: pytest
- Contenerización: Docker
- Despliegue: Render (solo si las pruebas pasan)

## 5. Verificación (conexión con el pipeline)
La especificación no es un documento estático: sus criterios de aceptación
se hacen cumplir automáticamente a través del pipeline. Cada criterio se
verifica con una prueba en test_app.py; el servidor de integración continua
(GitHub Actions) ejecuta esas pruebas en cada cambio; y el despliegue en
Render se realiza únicamente si las pruebas pasan. De esta forma, ningún
cambio que viole la especificación llega a producción.