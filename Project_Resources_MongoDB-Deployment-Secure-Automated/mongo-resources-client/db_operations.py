from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Configuración de MongoDB
MONGO_URI = "mongodb://frodo:bolson@mongo-primary:27017/"
client = MongoClient(MONGO_URI)
db = client.test

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/comments')
def comments():
    comments = list(db.comments.find())
    return render_template('comments.html', comments=comments)

@app.route('/movies')
def movies():
    movies = list(db.movies.find())
    return render_template('movies.html', movies=movies)

@app.route('/sessions')
def sessions():
    sessions = list(db.sessions.find())
    return render_template('sessions.html', sessions=sessions)

@app.route('/theaters')
def theaters():
    theaters = list(db.theaters.find())
    return render_template('theaters.html', theaters=theaters)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

