#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Earth
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
RADIUS = 6.371
APOAPSIS = 152100000000
PERIAPSIS = 147095000000
LONGTITUDE_ASCENDING_NODE = -0.196535244
ARGUMENT_OF_PERIAPSIS = 1.993302665
INCLINATION = 0.000000873
INITIAL_MEAN_ANOMALY = 6.259047404
MULTIPLIER = 0.00000000
AXIAL_TILT = 0.409092629
SIDEREAL_ROTATION_PERIOD = 0.99726968
MASS = 5.97237e+2

class Earth(object):

    def create_earth(self, parent=None):
        name = "Earth"
        texture_name = "earth.jpg"

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