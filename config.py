import os


SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
BASE_DIR= os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQL_ALCHEMY_DATABASE_URI = 'your psycopg2 URI connection'

# Turn off the Flask-SQLAlchemy event system and warning
SQL_ALCHEMY_TRACK_MODIFICATIONS = False