#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Neptune
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
RADIUS = 12.311
APOAPSIS = 4.54e+12
PERIAPSIS = 4.46e+12
LONGTITUDE_ASCENDING_NODE = 2.300064701
ARGUMENT_OF_PERIAPSIS = 4.822973042
INCLINATION = 0.030856985
INITIAL_MEAN_ANOMALY = 4.472022236
MULTIPLIER = 0.000000001
AXIAL_TILT = 0.494277244
SIDEREAL_ROTATION_PERIOD = 0.6713
MASS = 1.0243e+29

class Neptune(object):

    def create_neptune(self, parent=None):
        name = "Neptune"
        texture_name = "neptune.jpg"

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