# Establece la imagen base como Python 3
FROM python:3

# Copia el contenido del directorio actual al directorio /app dentro del contenedor
COPY . /app

# Establece /app como el directorio de trabajo actual dentro del contenedor
WORKDIR /app

# Expone el puerto 5000 para que sea accesible
EXPOSE 5000

# Comando a ejecutar cuando se inicie el contenedor
CMD [ "python", "index.py" ]
