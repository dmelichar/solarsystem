#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ToDo: Documentation
""" A simple camera
A rather long blablabla
"""

from math import floor
from time import time

from util import auto_str


__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

@auto_str
class FPSCounter(object):
    """
    Class for the FPSCounter in the upper left corner
    """
    update_period = 0.25

    def __init__(self, window, update_fn=None):
        """
        Initializes the FPSCounter instances
        :param window: window instance
        :param update_fn: Function that gets called when the fps is updated
        """
        self.window = window
        self.update_fn = update_fn
        self._window_flip = window.flip
        window.flip = self._hook_flip

        self.time = 0.0
        self.last_time = time()
        self.count = 0
        self.fps = 0

    def update(self):
        """
        updates the current fps
        """
        from time import time
        t = time()
        self.count += 1
        self.time += t - self.last_time
        self.last_time = t

        if self.time >= self.update_period:
            self.set_fps(self.count / self.update_period)
            self.time %= self.update_period
            self.count = 0

    def set_fps(self, fps):
        """
        sets the FPS
        :param fps: new FPS
        """
        self.fps = fps
        if self.update_fn:
            self.update_fn(floor(self.fps))

    def _hook_flip(self):
        self.update()
        self._window_flip()