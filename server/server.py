from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

psql_user = 'niyaz'
psql_password = '12345'
psql_host = 'db'
psql_port = '5432'
psql_database = 'answersdb'
uri = f'postgresql://{psql_user}:{psql_password}@{psql_host}:{psql_port}/{psql_database}'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
