#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Concrete astronomical Objects
In this file, we have defined two of the major classes of
astronomical Objects, the ones that move and the ones that
seemingly don't. In theory, you could add more objects in
this file for whatever your needs are.
"""

from euclid3 import Vector3
from pyglet.gl import *
from pyglet.graphics import Batch
from astronomical_objects.AstronomicalObject import AstronomicalObject
from solar_system_renderer.Renderers import AOOrbitingRenderer

__author__ = "Sarah Kreutzer"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sarah Kreutzer"
__email__ = "skreutzer@student.tgm.ac.at"
__status__ = "Deployed"


class OrbitalObject(AstronomicalObject):
    """
    An astronomical Object which moves around another
    """

    def __init__(self, parent, name, texture_name, radius, axial_tilt, sidereal_rotation_period, mass, orbit,
                 renderer=AOOrbitingRenderer()):
        """
        Create a new orbiting astronomical Object

        :param parent: The objects parent (i.e. Sun for Earth)
        :param name: Name of the object (Earth, Saturn, Pluto, ...)
        :param texture_name: Name of the texture in the `res` directory
        :param radius: Radius of object
        :param axial_tilt: In astronomy, axial tilt is the angle between a planet's rotational axis at
        its north pole and a line perpendicular to the orbital plane of the planet - given in degrees.
        :param sidereal_rotation_period: The time required (in days) for a body within the solar system to complete
        one revolution with respect to the fixed stars—i.e., as observed from some fixed point outside the system.
        :param mass: Mass of the object in kilograms
        :param orbit: Orbit Class of this body
        """

        super().__init__(parent, name, texture_name, radius, axial_tilt, sidereal_rotation_period, mass,
                         renderer=renderer)
        self.orbit = orbit
        self.orbit.body = self
        self.orbit_line_batch = Batch()

    def config(self):
        """
        Configure the Object
        """

        self.orbit.config()
        orbit_line = []
        for pos in self.orbit.pos(1024):
            orbit_line.append(pos.x)
            orbit_line.append(pos.y)
            orbit_line.append(pos.z)
        self.orbit_line_batch.add(int(len(orbit_line) / 3), GL_LINE_LOOP, None, ('v3f', tuple(orbit_line)))

    def update(self, time):
        """
        Update the time in the solar system and
        position the object on its right coordinates

        :param time: Current solar time
        """

        super().update(time)
        self.xyz = self.orbit.calculate(time)
        #if self.parent:
           # self.xyz += self.parent.xyz


class StationaryObject(AstronomicalObject):
    """
    An astronomical Object that seemingly doesn't move in the system
    """

    def config(self):
        pass

    def __init__(self, parent, name, texture_name, radius, axial_tilt, sidereal_rotation_period, mass, xyz=Vector3()):
        """
        Create a new stationary astronomical Object

        :param parent: The objects parent (i.e. Sun for Earth)
        :param name: Name of the object (Earth, Saturn, Pluto, ...)
        :param texture_name: Name of the texture in the `res` directory
        :param radius: Radius of object
        :param axial_tilt: In astronomy, axial tilt is the angle between a planet's rotational axis at
        its north pole and a line perpendicular to the orbital plane of the planet - given in degrees.
        :param sidereal_rotation_period: The time required (in days) for a body within the solar system to complete
        one revolution with respect to the fixed stars—i.e., as observed from some fixed point outside the system.
        :param mass: Mass of the object in kilograms
        :param xyz: Position of the object, default 0, 0, 0
        """

        super().__init__(parent, name, texture_name, radius, axial_tilt, sidereal_rotation_period, mass)
        self.xyz = xyz
