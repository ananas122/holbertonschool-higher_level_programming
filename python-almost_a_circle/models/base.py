#!/usr/bin/python3
""" A module class Base """
import json
import os


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

        # Convertir les obj en dict en utilisant la méthode to_dictionary()
        dictionaries = [obj.to_dictionary() for obj in list_objs]

        # Ouvrir le fichier en mode écriture
        with open(filename, mode="w", encoding="utf-8") as file:
            # Utiliser la fonction json.dump pour écrire les dict dans le f
            json.dump(dictionaries, file)

    def from_json_string(json_string):
        """Create a new instance of the class from a json string """
        if json_string is None or json_string is []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set"""
        # Vérifie le type de classe pour déterminer l'instance à créer
        if cls.__name__ == "Rectangle":
            # Si class == Rectangle, crée une instance avec une lrg et H de 1
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            # Si la classe est Square, crée une instance avec un côté de 1
            dummy = cls(1)
        else:
            # Pour les autres dérivées de Base, crée une instance par défaut
            dummy = cls()

        # MAJr les attr de l'instance en utilisant les valeurs du dictionary
        dummy.update(**dictionary)

        # Retourne l'instance avec tous les attributs déjà définis
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                json_data = file.read()
                data = Base.from_json_string(json_data)
                return [cls.create(**item) for item in data]
        return []

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances """
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename):
            # Ouvrir le fichier en mode lecture
            with open(filename, 'r') as file:
                # Lire les données JSON du fichier
                json_data = file.read()
                # Convertir les données JSON en objet Base
                data = Base.from_json_string(json_data)
                # Créer une lst d'objets de la classe actu
                return [cls.create(**item) for item in data]
        # Si le fichier n'existe pas, retourner une liste vide
        return []
