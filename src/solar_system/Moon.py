#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Earth's moon
"""
from astronomical_objects.AstronomicalObjects import OrbitalObject
from astronomical_orbits.AstronomicalOrbits import CircularOrbit
from util import DAYS_TO_SECONDS

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

# Physical constants
RADIUS = 15.36
ORBITAL_PERIOD = 29.530589
INCLINATION = 0.08979719
AXIAL_TILT = 0.116710167
SIDEREAL_ROTATION_PERIOD = 27.321582
MASS = 7.349e+25

class Moon(object):

    def create_moon(self, parent=None):
        name = "Moon"
        texture_name = "moon.jpg"

        orbit = CircularOrbit(RADIUS, ORBITAL_PERIOD, INCLINATION)

        object = OrbitalObject(parent,
                             name,
                             texture_name,
                             RADIUS,
                             AXIAL_TILT,
                             SIDEREAL_ROTATION_PERIOD * DAYS_TO_SECONDS,
                             MASS,
                             orbit)

        object.parent = parent
        object.config()
        return object