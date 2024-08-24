#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        di = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(di, json_file, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel

        cls = {'BaseModel': BaseModel}

        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for key, obj in data.items():
                    FileStorage.__objects[key] = cls[obj['__class__']](**obj)
        except FileNotFoundError:
            pass
