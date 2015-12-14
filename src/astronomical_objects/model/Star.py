#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Concrete model for the astronomical Object: Star

Using this class allows for a structured implementation of
a solar system.
"""
from astronomical_objects.model.AstronomicalObject import AstronomicalObject

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"


class Star(AstronomicalObject):
    def __int__(self, name = "Sun", texture = None, period_of_orbit = 0, radius_of_orbit = 0, radius_of_object = 695500):
        """

        :param name: Star name
        :param texture: Name to the texture that shall be applied (note: needs to be in res folder)
        :param period_of_orbit: This has to be 0
        :param radius_of_orbit: This has to be 0
        :param radius_of_object: Radius of the star in kilometers
        :return:
        """
        self.name = self.name(name)
        self.texture = self.texture(texture)
        self.radius_of_orbit = self.radius_of_orbit(radius_of_orbit)
        self.period_of_orbit = self.period_of_orbit(period_of_orbit)
        self.radius_of_object = self.radius_of_object(radius_of_object)

    def type(self):
        self.type = super().type('Star')

    def name(self, name):
        self.name = super().name(name)

    def texture(self, name):
        self.texture = super().texture(name)

    def period_of_orbit(self, radius):
        period_of_orbit = super().period_of_orbit(radius)
        if period_of_orbit > 0:
            raise ValueError('A sun is normally stationary, please set the period_of_orbit variable to 0')
        else:
            self.period_of_orbit = period_of_orbit

    def radius_of_orbit(self, radius):
        radius_of_orbit = super().radius_of_orbit(radius)
        if radius_of_orbit > 0:
            raise ValueError('A sun is normally stationary, please set the radius_of_orbit variable to 0')
        else:
            self.radius_of_orbit = radius_of_orbit

    def radius_of_object(self, radius):
        self.radius_of_object = super().radius_of_object(radius)

if __name__ == "main":
    pass
