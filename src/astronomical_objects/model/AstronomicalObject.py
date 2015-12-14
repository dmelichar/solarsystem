#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bla bla bla
"""

from abc import ABCMeta, abstractmethod
import os.path
import imghdr

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

RESOURCES = os.path.join(os.path.dirname(__file__), '..', '..', 'res')

class AstronomicalObject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def type(self, type):
        allowed_types = ['Asteroid', 'Moon', 'Planet', 'Star']
        if type in allowed_types:
            return type
        else:
            raise TypeError('Unsupported type of astronomical Object - you may only use: {0}'.format(allowed_types))

    @property
    @abstractmethod
    def texture(self, name):
        texture = os.path.join(RESOURCES, name)
        texture_type = imghdr.what(texture)

        if os.path.exists(texture):
            if texture_type == 'jpeg':
                return texture
            elif texture_type == 'png':
                return texture
            else:
                raise TypeError('Unsupported image type detected - please use jpeg or png!')
        else:
            raise FileNotFoundError('Could not find specified texture!')

    @property
    @abstractmethod
    def name(self, name):
        return name
        # TODO: Check for compatibility

    @property
    @abstractmethod
    def radius_of_object(self, radius):
        if isinstance(radius, (int, float)):
            return radius
        else:
            raise TypeError('The radius of an astronomical Object has to be a number!')

    @property
    @abstractmethod
    def period_of_orbit(self, radius):
        if isinstance(radius, (int, float)):
            return radius
        else:
            raise TypeError('The period of an astronomical Object\'s orbit has to be a number!')

    @property
    @abstractmethod
    def radius_of_orbit(self, radius):
        if isinstance(radius, (int, float)):
            return radius
        else:
            raise TypeError('The radius of an astronomical Object\'s orbit has to be a number!')


if __name__ == "main":
    print(RESOURCES)
