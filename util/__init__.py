#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ToDo: Documentation
""" Blabla
A rather long blablabla

"""

import ctypes
import time as time_
from math import pi

from pyglet.gl import GLdouble

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

LIGHT = ctypes.c_float * 4
DAYS_TO_SECONDS = 24 * 60 * 60
PI_HALF = pi / 2.0

def auto_str(cls):
    """
    Adds an automatically generated __str__ method to the class that is annotated with it.
    :param cls: Class to annotate
    :return: Class that was annotated
    """

    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls


def millis():
    """
    Get the current time in milliseconds since epoch
    :return: Current time in milliseconds since epoch
    :rtype: int
    """

    return int(round(time_.time() * 1000))


def toGlMatrix(matrix4):
    """
    Converts the given matrix to be used by OpenGL
    :param matrix4: Matrix to convert
    :type matrix4: :class:`euclid.Matrix4`
    :return: Matrix to be used by OpenGL
    :rtype: No Idea
    """
    return (GLdouble * 16)(*matrix4)
