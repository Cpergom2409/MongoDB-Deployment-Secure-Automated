from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from db_operations import get_all_users, insert_user, update_user_password  # Importamos las funciones

app = Flask(__name__)

# Configuración de MongoDB
MONGO_URI = "mongodb://frodo:bolson@mongo-primary:27017/"
client = MongoClient(MONGO_URI)
db = client.test

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']

    try:
        # Conexión a MongoDB para autenticar
        user = db.users.find_one({"username": username})

        if user and user['password'] == password:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Credenciales incorrectas")
    except ConnectionFailure:
        return render_template('login.html', error="No se puede conectar a MongoDB")

@app.route('/dashboard')
def dashboard():
    # Usamos la función para obtener todos los usuarios
    users = get_all_users()
    return render_template('dashboard.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    # Obtenemos los datos del formulario
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Insertamos el nuevo usuario
    insert_user(username, email, password)
    
    # Redirigimos al dashboard después de agregar al usuario
    return redirect(url_for('dashboard'))

@app.route('/update_password', methods=['POST'])
def update_password():
    username = request.form['username']
    new_password = request.form['new_password']
    
    # Actualizamos la contraseña del usuario
    update_user_password(username, new_password)
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

