#!/usr/bin/python3
""" Write a function that reload json """
import json


class Student:
    """ Define a class students """
    def __init__(self, first_name, last_name, age):
        """initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        # Vérifie si attrs est une liste de str
        if type(attrs) is list and all(type(key) is str for key in attrs):

            # Crée un new dict vide pour stocker les attributs choisis
            new_dict = {}

            # Parcourt K et V
            for key, value in self.__dict__.items():

                # Si K est dans la liste des attributs choisis
                if key in attrs:

                    # Ajoute K et V au new_dict
                    new_dict[key] = value

            return new_dict
        else:

            # Si attrs n'est pas une l de str, return le dict de l'objet
            return self.__dict__

    def reload_from_json(self, json):
        """ reloads from json """
        self.__dict__.update(json)
