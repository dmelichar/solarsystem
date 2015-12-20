#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ToDo: Documentation
""" A simple camera
A rather long blablabla
"""
import pyglet
from pyglet.gl import *
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
class Texture(object):

    def __init__(self, filename, mipmaps=False):
        self.mipmaps = mipmaps
        self.filename = filename

        self.image = pyglet.resource.image(self.filename)
        self.texture = self.image.texture
        self._verify('width')
        self._verify('height')

        if self.mipmaps:
            glGenerateMipmap(self.texture.target)

    def draw(self):
        glEnable(self.texture.target)
        glBindTexture(self.texture.target, self.texture.id)
        if self.mipmaps:
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)

    def _verify(self, dimension):
        value = self.texture.__getattribute__(dimension)
        while value > 1:
            div_float = float(value) / 2.0
            div_int = int(div_float)
            if not (div_float == div_int):
                raise Exception('image %s is %d, which is not a power of 2' % (
                    dimension, self.texture.__getattribute__(dimension)))
            value = div_int