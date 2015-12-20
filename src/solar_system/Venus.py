#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Venus
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
RADIUS = 6.051
APOAPSIS = 108939000000
PERIAPSIS = 107477000000
LONGTITUDE_ASCENDING_NODE = 1.33831847
ARGUMENT_OF_PERIAPSIS = 0.957906507
INCLINATION = 0.059246598
INITIAL_MEAN_ANOMALY = 0.874671755,
MULTIPLIER = 0.000000001
AXIAL_TILT = 0.0460766923
SIDEREAL_ROTATION_PERIOD = -243.025
MASS = 4.869e+27

class Venus(object):

    def create_venus(self):
        name = "Venus"
        texture_name = "venus.jpg"

        orbit = EllipticalOrbit(APOAPSIS,
                               PERIAPSIS,
                               LONGTITUDE_ASCENDING_NODE,
                               ARGUMENT_OF_PERIAPSIS,
                               INCLINATION,
                               INITIAL_MEAN_ANOMALY,
                               MULTIPLIER)

        object = OrbitalObject(None,
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