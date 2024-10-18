import os  # Importa el módulo os para interactuar con el sistema operativo
from http.server import SimpleHTTPRequestHandler, HTTPServer  # Importa clases para manejar solicitudes HTTP

# Contenido HTML que se servirá cuando se acceda al servidor
html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>Python Docker</title>
  </head>
  <body>
    <h1>¡Hola mundo sin Flask desde un Docker!</h1>
  </body>
</html>
"""

# Clase que maneja las solicitudes HTTP y sirve el contenido HTML definido
class HTMLServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Envia una respuesta HTTP 200 (OK)
        self.send_response(200)
        # Establece el tipo de contenido en HTML
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Escribe el contenido HTML en el cuerpo de la respuesta
        self.wfile.write(html_content.encode())

# Función para ejecutar el servidor HTTP
def run(server_class=HTTPServer, handler_class=HTMLServer, port=5000):
    # Dirección del servidor y puerto en el que se escucharán las solicitudes
    server_address = ('', port)
    # Crea una instancia del servidor HTTP con la clase proporcionada
    httpd = server_class(server_address, handler_class)
    # Muestra un mensaje para indicar que el servidor está en ejecución
    print(f'Servidor HTTP sirviendo en el puerto {port}...')
    # Inicia el servidor y comienza a escuchar las solicitudes entrantes
    httpd.serve_forever()

# Se ejecuta el servidor si el script es el programa principal
if __name__ == "__main__":
    run()  # Llama a la función run() para iniciar el servidor
