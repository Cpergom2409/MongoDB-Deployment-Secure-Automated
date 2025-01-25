from pymongo import MongoClient

# Configuración de MongoDB
MONGO_URI = "mongodb://frodo:bolson@mongo-primary:27017/"
client = MongoClient(MONGO_URI)
db = client.test

def get_all_users():
    """
    Recupera todos los usuarios de la base de datos.
    """
    users = db.users.find()
    return list(users)

def insert_user(username, email, password):
    """
    Inserta un nuevo usuario en la base de datos.
    """
    new_user = {
        "username": username,
        "email": email,
        "password": password
    }
    db.users.insert_one(new_user)

def update_user_password(username, new_password):
    """
    Actualiza la contraseña de un usuario.
    """
    db.users.update_one(
        {"username": username},
        {"$set": {"password": new_password}}
    )

