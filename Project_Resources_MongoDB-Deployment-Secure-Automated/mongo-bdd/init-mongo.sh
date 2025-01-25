#!/bin/bash

# Esperar hasta que MongoDB esté disponible
echo "Esperando a que MongoDB esté listo..."
sleep 10

# Cargar las bases de datos
echo "Importando datos..."

mongoimport --username frodo --password bolson --authenticationDatabase admin --db test --collection comments --file /data/import/comments.json --jsonArray
mongoimport --username frodo --password bolson --authenticationDatabase admin --db test --collection movies --file /data/import/movies.json --jsonArray
mongoimport --username frodo --password bolson --authenticationDatabase admin --db test --collection sessions --file /data/import/sessions.json --jsonArray
mongoimport --username frodo --password bolson --authenticationDatabase admin --db test --collection theaters --file /data/import/theaters.json --jsonArray
mongoimport --username frodo --password bolson --authenticationDatabase admin --db test --collection users --file /data/import/users.json --jsonArray

echo "Datos importados con éxito."

