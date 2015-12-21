#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file serves the purpose of defining a
structure which has to be followed by all astronomical
objects which have to inherit it in order to work.
"""

from abc import ABCMeta, abstractmethod
from euclid3 import Vector3
from solar_system_renderer.Renderers import AORenderer
from util.Texture import Texture
from pyglet.gl import *
from util import auto_str

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Deployed"


@auto_str
class AstronomicalObject(object):
    """
    Abstract base class which defines structure
    """
    __metaclass__ = ABCMeta

    def __init__(self, parent, name, texture_name, radius, axial_tilt, sidereal_rotation_period, mass, renderer=AORenderer()):
        """
        Create a new astronomical Object.

        :param parent: The objects parent (i.e. Sun for Earth)
        :param name: Name of the body (Earth, Saturn, Pluto, ...)
        :param texture_name: Name of the texture in the `res` directory
        :param radius: Radius of object
        :param axial_tilt: In astronomy, axial tilt is the angle between a planet's rotational axis at
        its north pole and a line perpendicular to the orbital plane of the planet - given in degrees.
        :param sidereal_rotation_period: The time required (in days) for a body within the solar system to complete
        one revolution with respect to the fixed stars—i.e., as observed from some fixed point outside the system.
        :param mass: Mass of the body in kilograms
        """
        self.xyz = Vector3()
        self.parent = parent
        self.name = name
        self.texture_name = texture_name
        self.radius = radius
        self.axial_tilt = axial_tilt
        self.sidereal_rotation_period = sidereal_rotation_period
        self.mass = mass
        self.renderer = renderer

        self.time = 0
        self.orbit_visible = True
        self.texture_visible = True

        self.texture = Texture(texture_name)
        self.sphere = gluNewQuadric()
        gluQuadricNormals(self.sphere, GLU_SMOOTH)
        gluQuadricTexture(self.sphere, GL_TRUE)

    @abstractmethod
    def config(self):
        """
        Configure the object (should be done by the objects)
        """
        pass

    def update(self, time):
        """
        Update the time in the solar system and
        position the object on its right coordinates

        :param time: Current solar time
        """
        self.time = (time % self.sidereal_rotation_period) / self.sidereal_rotation_period

    def draw(self, matrix):
        """
        Draw the astronomical Object
        :param matrix: Matrix to draw
        """
        self.renderer.draw(self, matrix)
