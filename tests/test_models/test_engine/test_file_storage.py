#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
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
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_all(self):
        """Test all method"""
        self.assertIsNot(FileStorage.all.__doc__, None,
                         "all method needs a docstring")
        self.assertTrue(len(FileStorage.all.__doc__) >= 1,
                        "all method needs a docstring")
    
    def test_new(self):
        """Test new method"""
        self.assertIsNot(FileStorage.new.__doc__, None,
                         "new method needs a docstring")
        self.assertTrue(len(FileStorage.new.__doc__) >= 1,
                        "new method needs a docstring")

    def test_save(self):
        """Test save method"""
        self.assertIsNot(FileStorage.save.__doc__, None,
                         "save method needs a docstring")
        self.assertTrue(len(FileStorage.save.__doc__) >= 1,
                        "save method needs a docstring")

    def test_reload(self):
        """Test reload method"""
        self.assertIsNot(FileStorage.reload.__doc__, None,
                         "reload method needs a docstring")
        self.assertTrue(len(FileStorage.reload.__doc__) >= 1,
                        "reload method needs a docstring")

    def test_delete(self):
        """Test delete method"""
        self.assertIsNot(FileStorage.delete.__doc__, None,
                         "delete method needs a docstring")
        self.assertTrue(len(FileStorage.delete.__doc__) >= 1,
                        "delete method needs a docstring")

    def test_close(self):
        """Test close method"""
        self.assertIsNot(FileStorage.close.__doc__, None,
                         "close method needs a docstring")
        self.assertTrue(len(FileStorage.close.__doc__) >= 1,
                        "close method needs a docstring")

    def test_get(self):
        """Test get method"""
        self.assertIsNot(FileStorage.get.__doc__, None,
                         "get method needs a docstring")
        self.assertTrue(len(FileStorage.get.__doc__) >= 1,
                        "get method needs a docstring")

    def test_count(self):
        """Test count method"""
        self.assertIsNot(FileStorage.count.__doc__, None,
                         "count method needs a docstring")
        self.assertTrue(len(FileStorage.count.__doc__) >= 1,
                        "count method needs a docstring")



class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
