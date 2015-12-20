#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mars
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
RADIUS = 3.398
APOAPSIS = 249200000000
PERIAPSIS = 206700000000
LONGTITUDE_ASCENDING_NODE = 0.864950271
ARGUMENT_OF_PERIAPSIS = 5.000403214
INCLINATION = 0.03228859
INITIAL_MEAN_ANOMALY = 0.338122636
MULTIPLIER = 0.000000001
AXIAL_TILT = 0.439648439
SIDEREAL_ROTATION_PERIOD = 1.025957
MASS = 6.419e+26

class Mars(object):

    def create_mars(self, parent=None):
        name = "Mars"
        texture_name = "mars.jpg"

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