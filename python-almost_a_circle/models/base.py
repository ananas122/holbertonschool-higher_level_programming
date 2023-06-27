#!/usr/bin/python3
""" A module class Base """
import json


class Base:
    """ A simple class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is a constructor function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a list of dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        # Vérifier si la liste d'objets est vide
        if not list_objs:
            return None

        # Créer le nom de fichier en utilisant le nom de la classe
        filename = f"{cls.__name__}.json"

        # Convertir les objets en dictionnaires en utilisant la méthode to_dictionary()
        dictionaries = [obj.to_dictionary() for obj in list_objs]

        # Ouvrir le fichier en mode écriture
        with open(filename, mode="w", encoding="utf-8") as file:
            # Utiliser la fonction json.dump pour écrire les dictionnaires dans le fichier
            json.dump(dictionaries, file)


    def from_json_string(json_string):
        """Create a new instance of the class from a json string """
        if not json_string:
            return "[]"
        return json.loads(json_string)
