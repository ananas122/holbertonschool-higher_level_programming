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
        # Vérifie le nom de la classe pour déterminer le type d'instance à créer
        if cls.__name__ == "Rectangle":
            # Si la classe est Rectangle, crée une instance avec une lrg et une H de 1
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            # Si la classe est Square, crée une instance avec un côté de 1
            dummy = cls(1)
        else:
            # Pour les autres classes dérivées de Base, crée une instance par défaut
            dummy = cls()

        # Met à jour les attributs de l'instance en utilisant les valeurs du dictionnaire
        dummy.update(**dictionary)

        # Retourne l'instance avec tous les attributs déjà définis
        return dummy
