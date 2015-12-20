#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Saturn
"""
from astronomical_objects.AstronomicalObjects import OrbitalObject
from astronomical_orbits.AstronomicalOrbits import EllipticalOrbit
from solar_system_renderer.Renderers import AOOrbitingWithPRRenderer, setup_ring_renderer
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
RADIUS = 11.6464
APOAPSIS = 1.509e+12
PERIAPSIS = 1.35e+12
LONGTITUDE_ASCENDING_NODE = 1.983828494
ARGUMENT_OF_PERIAPSIS = 5.923507855
INCLINATION = 0.043375621
INITIAL_MEAN_ANOMALY = 5.533042795
MULTIPLIER = 0.000000001
AXIAL_TILT = 0.466526509
SIDEREAL_ROTATION_PERIOD = 0.4395
MASS = 5.685e+29

# Physical constants for Saturn's ring
radius_inner = 12
radius_outer = 28

class Saturn(object):

    def create_saturn(self, parent=None):
        name = "Saturn"
        texture_name = "saturn.jpg"
        ring_texture_name = "saturn_ring.png"

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

        object.renderer = AOOrbitingWithPRRenderer()
        object = setup_ring_renderer(ring_texture_name, radius_inner, radius_outer, object)

        object.parent = parent
        object.config()
        return object