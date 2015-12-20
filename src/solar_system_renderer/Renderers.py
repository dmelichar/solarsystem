#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Concrete Renderer Classes
In this file, we have defined two of the major renderer classes of
astronomical Orbits and their orbits: the ones that are stationary
and the ones that orbit around something. They inherit from the
AORenderer (Astronomical Objects Renderer) which doesn't consider
an orbit. In theory, you could create other Renderes to create
any other objects (e.g. Starships)
"""

from math import radians
from random import randint
from solar_system_renderer.Renderer import Renderer
from euclid3 import Vector3
from util import toGlMatrix
from util.Texture import Texture
from pyglet.gl import *

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

# Lambda function for random color generation
r = lambda: randint(0, 255)


class AORenderer(Renderer):
    """
    Renders an object at a fixed position with the given matrix
    """

    def draw(self, body, matrix):
        matrix.translate(body.xyz.x, body.xyz.y, body.xyz.z)
        matrix.rotate_axis(radians(-90), Vector3(1, 0, 0))
        matrix.rotate_axis(body.axial_tilt, Vector3(0, 1, 0))
        matrix.rotate_axis(radians(-360 * body.time), Vector3(0, 0, 1))
        glLoadMatrixd(toGlMatrix(matrix))
        if body.texture_visible:
            body.texture.draw()
        else:
            glColor3f(r(), r(), r())

        gluSphere(body.sphere, body.radius, 50, 50)
        glDisable(GL_TEXTURE_2D)


class AOOrbitingRenderer(AORenderer):
    """
    Renderer for orbiting astronomical Objects
    """
    def draw(self, body, matrix):
        if body.orbit_visible:
            linematrix = matrix.__copy__()
            if body.parent is not None:
                linematrix.translate(body.parent.xyz.x, body.parent.xyz.y, body.parent.xyz.z)

            glLoadMatrixd(toGlMatrix(linematrix))
            glLineWidth(1.25)
            glColor3f(r(), r(), r())
            body.orbit_line_batch.draw()

        glColor3f(1.0, 1.0, 1.0)

        super().draw(body, matrix)


class AOOrbitingWithPRRenderer(AORenderer):
    """
    Renderer for orbiting astronomical Objects with planetary rings
    """


    def draw(self, body, mat):
        if body.texture_visible:
            matrix = mat.__copy__()
            matrix.translate(body.xyz.x, body.xyz.y, body.xyz.z)
            matrix.rotate_axis(radians(-90), Vector3(1, 0, 0))
            matrix.rotate_axis(body.axial_tilt, Vector3(0, 1, 0))
            glLoadMatrixd(toGlMatrix(matrix))
            glDisable(GL_DEPTH_TEST)
            glDisable(GL_CULL_FACE)
            body.ring_texture.draw()
            gluDisk(body.ring_disk, body.ring_inner_radius, body.ring_outer_radius, 50, 50)
            glEnable(GL_CULL_FACE)
            glEnable(GL_DEPTH_TEST)
            glDisable(GL_TEXTURE_2D)

        super().draw(body, mat)


def setup_ring_renderer(ring_texture_name, ring_inner_radius, ring_outer_radius, body):
    """
    Sets the needed parameters for the OrbitingBodyWithRingRenderer.

    :param ring_texture_name: Name of the texture
    :type ring_texture_name: str
    :param ring_inner_radius: Inner radius of the rings
    :type ring_inner_radius: float
    :param ring_outer_radius: Outer radius of the rings
    :type ring_outer_radius: float
    :param body: Body to apply these parameters to
    :type body: :class:`solarsystem.body.Body`
    :return: Supplied body
    :rtype: :class:`solarsystem.body.Body`
    """

    body.ring_inner_radius = ring_inner_radius
    body.ring_outer_radius = ring_outer_radius
    body.ring_texture = Texture(ring_texture_name)
    body.ring_disk = gluNewQuadric()
    gluQuadricNormals(body.ring_disk, GLU_SMOOTH)
    gluQuadricTexture(body.ring_disk, GL_TRUE)
    return body
