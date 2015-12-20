#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pluto (yes, it is)
"""
from astronomical_objects.AstronomicalObjects import OrbitalObject
from astronomical_orbits.AstronomicalOrbits import EllipticalOrbit
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
RADIUS = 3.561
APOAPSIS = 7.37593e+14
PERIAPSIS = 4.43682e+14
LONGTITUDE_ASCENDING_NODE = 1.925080712
ARGUMENT_OF_PERIAPSIS = 1.986778101
INCLINATION = 0.29915816
INITIAL_MEAN_ANOMALY = 0.25359634
MULTIPLIER = 0.000000000025
AXIAL_TILT = 2.08725671
SIDEREAL_ROTATION_PERIOD = 6.387230
MASS = 1.303e+25

class Pluto(object):

    def create_pluto(self, parent=None):
        name = "Pluto"
        texture_name = "pluto.jpg"

        orbit = EllipticalOrbit(APOAPSIS,
                               PERIAPSIS,
                               LONGTITUDE_ASCENDING_NODE,
                               ARGUMENT_OF_PERIAPSIS,
                               INCLINATION,
                               INITIAL_MEAN_ANOMALY,
                               MULTIPLIER)

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