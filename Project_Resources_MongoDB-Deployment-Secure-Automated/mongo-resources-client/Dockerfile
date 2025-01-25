FROM python:3.9-slim

WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . /app

# Instalar las dependencias necesarias
RUN pip install pymongo flask

# Ejecutar el script Python (en lugar de validate.py)
CMD ["python", "db_operations.py"]

