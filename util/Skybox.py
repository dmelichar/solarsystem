#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ToDo: Documentation
""" A simple camera
A rather long blablabla
"""
from pyglet.gl import *
from util import auto_str
from util.Texture import Texture

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

@auto_str
class SkySphere():
    """
    A SkyBox that maps the texture to a sphere
    """

    def __init__(self, filename, radius):
        """
        Creates a new SkyShpere
        :param filename: Filename of the texture
        :type filename: str
        :param radius: Radius of the skysphere
        :type radius: float
        """

        self.radius = radius
        self.texture = Texture(filename)
        self.sphere = gluNewQuadric()
        gluQuadricNormals(self.sphere, GLU_SMOOTH)
        gluQuadricTexture(self.sphere, GL_TRUE)

    def draw(self):
        """
        Draws the SkySphere
        """

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)
        glDisable(GL_CULL_FACE)
        self.texture.draw()
        gluSphere(self.sphere, self.radius, 50, 50)