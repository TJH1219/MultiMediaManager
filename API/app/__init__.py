from flask import Flask
from .Database.DatabaseManager import DatabaseManager
from os import path,makedirs

app = Flask(__name__)

# Create data directory if it doesn't exist
db_dir = path.join(path.dirname(__file__), 'data')
makedirs(db_dir, exist_ok=True)

# Initialize database manager with full path
db_path = path.join(db_dir, 'multimedia.db')
db_manager = DatabaseManager(db_path)

from . import routes
