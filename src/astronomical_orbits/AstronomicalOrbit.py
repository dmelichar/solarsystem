#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file serves the purpose of defining a
structure which has to be followed by all orbits of
astronomical objects which have to inherit this in
order to work.
"""

from abc import ABCMeta, abstractmethod
from util import auto_str

__author__ = "Sarah Kreutzer"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sarah Kreutzer"
__email__ = "skreutzer@student.tgm.ac.at"
__status__ = "Deployed"

@auto_str
class AstronomicalOrbit(object):
    """
    Abstract base class which defines structure
    """
    __metaclass__ = ABCMeta

    def __init__(self, body=None, multiplier=1):
        """
        Create a new orbit for an astronomical Object

        :param body: The astronomical object which orbits
        :param multiplier: Position multiplier
        """
        self.body = body
        self.multiplier = multiplier

    @abstractmethod
    def config(self):
        """
        Configure the object (should be done by the objects)
        """
        pass

    @abstractmethod
    def calculate(self, time):
        """
        Calculate current position of body with the current time and return it

        :param time: Delta time
        :return: position
        """
        pass

    def pos(self, steps):
        """
        Generator to calculate the position in orbit

        :param steps: Steps to calculate
        :return: int
        """
        step = self.orbital_period / steps
        for i in range(0, steps):
            yield self.calculate(i * step)
