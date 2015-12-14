#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Concrete model for the astronomical Object: Planet

Using this class allows for a structured implementation of
a solar system. With this class, you can build asteroid fields
among other things. The default values come from Earth.

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


class Planet(AstronomicalObject):
    def __int__(self, name = "Earth", texture = None, period_of_orbit = 365, radius_of_orbit = 150, radius_of_object = 6371, moons = None):
        """

        :param name: Planet name
        :param texture: Name to the texture that shall be applied (note: needs to be in res folder)
        :param period_of_orbit: Days until the Planet has reached around the sun once
        :param radius_of_orbit: Kilometers of the Planet path around the sun
        :param radius_of_object: Radius of the Planet in kilometers
        :return:
        """
        self.name = self.name(name)
        self.texture = self.texture(texture)
        self.radius_of_orbit = self.radius_of_orbit(radius_of_orbit)
        self.period_of_orbit = self.period_of_orbit(period_of_orbit)
        self.radius_of_object = self.radius_of_object(radius_of_object)
        # self.moons # Needs implementation

    def type(self):
        self.type = super().type('Planet')

    def name(self, name):
        self.name = super().name(name)

    def texture(self, name):
        self.texture = super().texture(name)

    def period_of_orbit(self, radius):
        self.period_of_orbit = super().periodg_of_orbit(radius)

    def radius_of_orbit(self, radius):
        self.radius_of_orbit = super().radius_of_orbit(radius)

    def radius_of_object(self, radius):
        self.radius_of_object = super().radius_of_object(radius)

if __name__ == "main":
    pass
