# Usa la imagen oficial de Python
FROM python:3.9-slim

# Setea el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . /app

# Instala las dependencias directamente
RUN pip install Flask pymongo

# Expone el puerto 5000
EXPOSE 5000

# Comando para correr el servidor Flask
CMD ["python", "validate.py"]

