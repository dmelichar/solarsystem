#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ToDo: Documentation
""" Blabla
A rather long blablabla
"""

import pyglet
from euclid3 import *
from pyglet.gl import *

import math
from solar_system.Earth import Earth
from solar_system.Mars import Mars
from solar_system.Mercury import Mercury
from solar_system.Moon import Moon
from solar_system.Neptune import Neptune
from solar_system.Pluto import Pluto
from solar_system.Saturn import Saturn
from solar_system.Sun import Sun
from solar_system.Uranus import Uranus
from solar_system.Venus import Venus
from solar_system_gui.Controls import Controls
from solar_system_gui.GUI import GUI
from util import toGlMatrix
from util.Camera import Camera, PI_HALF
from util.Skybox import SkySphere

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Production"

# Register resource locations in pyglet resource loader
pyglet.resource.path = ['res/textures', 'res/gui']
pyglet.resource.reindex()

# Configure and setup window
config = pyglet.gl.Config(sample_buffers=1, samples=8, depth_size=24)
window = pyglet.window.Window(1280, 720, config=config, caption='Solar System', resizable=True, vsync=False)

fullscreen = False
draw_skybox = True

# looad the bodies from the json files
sun = Sun().create_sun()
earth = Earth().create_earth(sun)
bodies = {sun,
         earth,
         Mars().create_mars(sun),
         Mercury().create_mercury(sun),
         Moon().create_moon(earth),
         Neptune().create_neptune(sun),
         Pluto().create_pluto(sun),
         Saturn().create_saturn(sun),
         Uranus().create_uranus(sun)}

print(bodies)


# Create a new camera
camera = Camera(position=Vector3(0, 420, 0), pitch=-PI_HALF)

# Create model and projection matrices
model_matrix = Matrix4()
proj_matrix = None
mvp = Matrix4()

# time
timestep = 0
solarsystem_time = 0
time = solarsystem_time

# create the skyshpere
skybox = SkySphere("milkyway.jpg", 5500)


def toggle_draw_orbits():
    """
    Toggles the plotting of the orbits
    """

    for cur in bodies:
        cur.draw_orbit = not cur.draw_orbit


def toggle_draw_textures():
    """
    Toggles the drawing of the textures
    """

    global draw_skybox
    draw_skybox = not draw_skybox
    for cur in bodies:
        cur.draw_texture = not cur.draw_texture


def toggle_fullscreen(override):
    global fullscreen
    if override is not None:
        fullscreen = override
    else:
        fullscreen = not fullscreen
    window.set_fullscreen(fullscreen)


controls = Controls(window, camera, bodies, callbacks={'toggle_draw_orbits': toggle_draw_orbits,
                                                       'toggle_draw_textures': toggle_draw_textures,
                                                       'toggle_fullscreen': toggle_fullscreen})

gui = GUI(window, controls, bodies)


@window.event
def on_resize(width, height):
    """
    Capture pyglet resize event

    :param width: New width
    :param height: New height
    """

    global proj_matrix
    # recalculate projection matrix
    proj_matrix = Matrix4.new_perspective(45, float(width) / float(height), 0.1, 64000.0)
    # set new viewport
    glViewport(0, 0, width, height)
    glMatrixMode(GL_MODELVIEW)


@window.event
def on_draw():
    """
    Redraw the screen
    """

    # reset window and set all needed opengl flags
    window.clear()
    glPushAttrib(GL_ENABLE_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)

    # draw skybox if requested
    if draw_skybox:
        glPushAttrib(GL_ENABLE_BIT)
        skybox_matrix = mvp.__copy__()
        skybox_matrix.translate(camera.position.x, camera.position.y, camera.position.z)
        skybox_matrix.rotate_axis(math.radians(-90), Vector3(1, 0, 0))
        glLoadMatrixd(toGlMatrix(skybox_matrix))
        skybox.draw()
        glPopAttrib()

    # loop through bodies and draw
    for planet in bodies:
        glPushAttrib(GL_ENABLE_BIT)
        planet.draw(mvp.__copy__())
        glPopAttrib()

    glPopAttrib()

    # ====== START GUI ======
    # create an orthographic projection (2d)
    glPushAttrib(GL_ENABLE_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glOrtho(0, window.width, 0, window.height, -1, 1)

    gui.draw()

    glColor3f(1, 1, 0)
    glLineWidth(1.0)
    glBegin(GL_LINES)
    cross_len = 10
    glVertex2f(window.width / 2 - cross_len, window.height / 2)
    glVertex2f(window.width / 2 + cross_len, window.height / 2)
    glVertex2f(window.width / 2, window.height / 2 - cross_len)
    glVertex2f(window.width / 2, window.height / 2 + cross_len)
    glEnd()
    glColor3f(1, 1, 1)

    glPopAttrib()
    # ====== STOP GUI ======


def update(dt):
    """
    Update time, Recalculate orbital positions

    :param dt: Time since last update
    """
    global solarsystem_time
    global mvp
    global time

    # recalculate solarsystem time
    timestep = 60 * 60 * 24 * 7 * controls.time_multiplier
    solarsystem_time += dt * timestep
    time += dt
    gui.update_time(timestep, solarsystem_time)

    if not controls.toggled_help_label and time >= 10:
        controls.draw_help_label = False

    # update the controls
    controls.update(dt)
    # recalculate mvp matrix
    mvp = proj_matrix * camera.view_matrix()

    # update every bodies
    for planet in bodies:
        planet.update(solarsystem_time)


# starts the application
pyglet.clock.schedule(update)
pyglet.app.run()