#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Uranus
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
RADIUS = 12.681
APOAPSIS = 3.008e+12
PERIAPSIS = 2.742e+12
LONGTITUDE_ASCENDING_NODE = 1.291648366
ARGUMENT_OF_PERIAPSIS = 1.692949425
INCLINATION = 0.013491395
INITIAL_MEAN_ANOMALY = 2.482531893
MULTIPLIER = 0.000000001
AXIAL_TILT = 1.70640841
SIDEREAL_ROTATION_PERIOD = 0.71833
MASS = 8.683e+28

class Uranus(object):

    def create_uranus(self, parent=None):
        name = "Uranus"
        texture_name = "uranus.jpg"

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