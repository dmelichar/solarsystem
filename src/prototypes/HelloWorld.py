#!/usr/bin/env python

"""
Basic HelloWorld Example in Pyglet.
"""

import pyglet

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Deployed"

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')


pyglet.app.run()


if __name__ == '__main__':    #code to execute if called from command-line
    pass    #do nothing - code deleted
#use this either for a simple example of how to use the module,
#or when the module can meaningfully be called as a script.