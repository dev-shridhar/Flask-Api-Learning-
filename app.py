from flask import Flask
from flask_rest import Api
from flask_restful import Resource,reqparse  
import sqlite3

app = Flask(__name__)
api = Api(app)

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
create_query = "CREATE TABLE users(id INT, username VARCHAR, password VARCHAR)"
cursor.execute(create_query)
connection.commit()
connection.close()

if __name__ == "__main__":
    app.run(debug=True)