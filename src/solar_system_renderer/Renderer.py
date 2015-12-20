#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Documentation

"""
The Renderer is responsible for the ordered
drawing of all astronomical Objects and their
orbits. It is not responsible for the GUI!
"""

from util import auto_str
from abc import ABCMeta, abstractmethod

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

@auto_str
class Renderer(object):
    """
    A base class for all renderers to inherit
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self, body, matrix):
        """
        Draw the body according the the matrix

        :param body: The body to render
        :param matrix:
        """
        pass
