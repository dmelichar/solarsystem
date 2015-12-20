#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mercury
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
RADIUS = 4.879
APOAPSIS = 69816900000
PERIAPSIS = 46001200000
LONGTITUDE_ASCENDING_NODE = 0.843535081
ARGUMENT_OF_PERIAPSIS = 0.508309691
INCLINATION = 0.122260314
INITIAL_MEAN_ANOMALY = 3.050765719
MULTIPLIER = 0.000000001
AXIAL_TILT = 0.000593411946
SIDEREAL_ROTATION_PERIOD = 58.646
MASS = 3.301e+26

class Mercury(object):

    def create_mercury(self, parent=None):
        name = "Mercury"
        texture_name = "mercury.jpg"

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