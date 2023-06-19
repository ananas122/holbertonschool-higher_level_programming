#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Define an area"""

    def area(self):
        """raise an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
