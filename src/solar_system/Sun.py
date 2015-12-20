#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sun
"""
from astronomical_objects.AstronomicalObjects import StationaryObject

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

# Physical constants
RADIUS = 12
AXIAL_TILT = 0.126536371
SIDEREAL_ROTATION_PERIOD = 25.83
MASS = 1.9884e+30


class Sun(object):
    def create_sun(self):
        name = "Sun"
        texture_name = "sun.jpg"

        object = StationaryObject(None, name, texture_name, RADIUS, AXIAL_TILT, SIDEREAL_ROTATION_PERIOD, MASS)

        object.config()
        return object
