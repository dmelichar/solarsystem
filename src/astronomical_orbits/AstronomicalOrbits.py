#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Concrete astronomical Orbits
In this file, we have defined two of the major classes of
astronomical Orbits: the ones that orbit around an object
in an elliptical fashion (like the Earth orbits the Sun) and
the ones that orbit around an object in an circular fashion
(like the Moon does around the Earth, more or less)
"""

from math import *

from euclid3 import Vector3
from util.Orbit import GRAVITY, true_anomaly_from_eccentric, eccentric_anomaly_from_mean
from astronomical_orbits.AstronomicalOrbit import AstronomicalOrbit

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"


class EllipticalOrbit(AstronomicalOrbit):
    """
    An elliptical Orbit
    """

    def __init__(self, apoapsis, periapsis, longtitude_ascending_node, argument_of_periapsis, inclination,
                 initial_mean_anomaly=0, multiplier=1):
        """
        Creates a new elliptical orbit from the given parameters

        :param apoapsis: Apoapsis in meters
        :param periapsis: Periapsis in meters
        :param longtitude_ascending_node: Longtitude of the ascending node in radians
        :param argument_of_periapsis: Argument of the periapsis in radians
        :param initial_mean_anomaly: Initial mean anomaly at J.2000 in radians
        :param inclination: Inclination of the orbit in radians
        """

        super().__init__(multiplier=multiplier)

        self.apoapsis = apoapsis
        self.periapsis = periapsis
        self.longtitude_ascending_node = longtitude_ascending_node
        self.argument_of_periapsis = argument_of_periapsis
        self.initial_mean_anomaly = initial_mean_anomaly
        self.inclination = inclination

    def calculate(self, time):
        """
        Calculate current position of body with the current time and return it

        :param time: Delta time
        :return: position
        """

        mean_anomaly = self.initial_mean_anomaly
        mean_anomaly += self.mean_motion * time
        true_anomaly = true_anomaly_from_eccentric(self.eccentricity,
                                                   eccentric_anomaly_from_mean(self.eccentricity, mean_anomaly))
        true_anomaly = abs(true_anomaly)
        radius = self.semi_major_axis * (1.0 - self.eccentricity ** 2.0) / (1.0 + self.eccentricity * cos(true_anomaly))
        x = radius * (cos(self.longtitude_ascending_node) * cos(true_anomaly + self.argument_of_periapsis) - sin(
            self.longtitude_ascending_node) * sin(true_anomaly + self.argument_of_periapsis) * cos(self.inclination))
        z = radius * (sin(self.longtitude_ascending_node) * cos(true_anomaly + self.argument_of_periapsis) + cos(
            self.longtitude_ascending_node) * sin(true_anomaly + self.argument_of_periapsis) * cos(self.inclination))
        y = radius * sin(true_anomaly + self.argument_of_periapsis) * sin(self.inclination)
        pos = Vector3(x, y, z)
        pos *= self.multiplier
        return pos

    def config(self):
        self.semi_major_axis = (self.apoapsis + self.periapsis) / 2.0
        self.eccentricity = (self.apoapsis - self.periapsis) / (self.apoapsis + self.periapsis)
        self.orbital_period = 2.0 * pi * sqrt(
            (self.semi_major_axis ** 3.0) / (GRAVITY * (5.97237 * 10 ** 24 + 1.9884 * 10 ** 30)))
        self.mean_motion = 2.0 * pi / self.orbital_period


class CircularOrbit(AstronomicalOrbit):
    """
    A circular Orbit
    """

    def __init__(self, radius, orbital_period, inclination=0, multiplier=1):
        """
        Create a new circular orbit based on the radius and the period

        :param radius: Radius of orbit
        :param orbital_period: Days of orbit's duration
        :param inclination: Orbital inclination is the angle (in radians)between a
        reference plane and the orbital plane or axis of direction of an
         object in orbit around another object.
        """

        super().__init__(multiplier=multiplier)
        self.radius = radius
        self.orbital_period = orbital_period
        self.inclination = inclination

    def calculate(self, time):
        """
        Calculate current position of body with the current time and return it

        :param time: Delta time
        :return: position
        """
        angle = radians(360 * ((time % self.orbital_period) / self.orbital_period))
        x = self.radius * cos(angle)
        z = self.radius * sin(angle)
        pos = Vector3(x, 0, z)
        if self.inclination != 0:
            pos = pos.rotate_around(Vector3(0, 0, 1), self.inclination)
        return pos

    def config(self):
        pass
