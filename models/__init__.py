#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from dotenv import load_dotenv

load_dotenv()

env_vars = ['HBNB_ENV','HBNB_MYSQL_USER','HBNB_MYSQL_PWD','HBNB_MYSQL_HOST',
            'HBNB_MYSQL_DB',]

for var in env_vars:
    if not os.getenv(var):
        raise Exception(f"Environment Varible {var} not found!")


storage_type = os.getenv('HBNB_TYPE_STORAGE')
storage = None

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()


storage.reload()
