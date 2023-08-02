import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Configuring a database for the Flask application defined above.
usuario = 'root'
contraseña = 'Namixluffy123#'
nombre_basedatos = 'ariadnePOC'
cadena_conexion = f'mysql+mysqlconnector://{usuario}:{contraseña}@127.0.0.1:3306/{nombre_basedatos}'

app.config["SQLALCHEMY_DATABASE_URI"] = cadena_conexion
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


# Annotation that allows for the endpoints / URL to be hit.
@app.route('/')
def hello_world():
	return 'Hello World!'