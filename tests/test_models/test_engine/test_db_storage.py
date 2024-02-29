#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_all(self):
        """Test all method"""
        storage = DBStorage()
        obj = storage.all()
        self.assertEqual(type(obj), dict)

    def test_all_cls(self):
        """Test all method with class"""
        storage = DBStorage()
        obj = storage.all(State)
        self.assertEqual(type(obj), dict)

    def test_new(self):
        """Test new method"""
        storage = DBStorage()
        state = State(name="California")
        storage.new(state)
        key = state.__class__.__name__ + "." + state.id
        obj = storage.all()
        self.assertTrue(key in obj)

    def test_save(self):
        """Test save method"""
        storage = DBStorage()
        state = State(name="California")
        storage.new(state)
        storage.save()
        with open("file.json", "r") as file:
            self.assertTrue(len(file.read()) > 0)


    def test_reload(self):
        """Test reload method"""
        storage = DBStorage()
        state = State(name="California")
        storage.new(state)
        storage.save()
        storage.reload()
        obj = storage.all()
        key = state.__class__.__name__ + "." + state.id
        self.assertTrue(key in obj)

    def test_delete(self):
        """Test delete method"""
        storage = DBStorage()
        state = State(name="California")
        storage.new(state)
        storage.save()
        storage.delete(state)
        obj = storage.all()
        self.assertFalse(state in obj.values())

    def test_get(self):
        """Test get method"""
        storage = DBStorage()
        state = State(name="California")
        storage.new(state)
        storage.save()
        obj = storage.get(State, state.id)
        self.assertEqual(obj, state)

    def test_count(self):
        """Test count method"""
        storage = DBStorage()
        state = State(name="California")
        storage.new(state)
        storage.save()
        count = storage.count(State)
        self.assertEqual(count, 1)

    def test_get_none(self):
        """Test get method with None"""
        storage = DBStorage()
        obj = storage.get(None, None)
        self.assertEqual(obj, None)

    def test_count_none(self):
        """Test count method with None"""
        storage = DBStorage()
        count = storage.count(None)
        self.assertEqual(count, 0)
class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
