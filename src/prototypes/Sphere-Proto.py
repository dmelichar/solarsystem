#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Trying to build a Sphere and a basic camera

In this file we're trying to use OpenGL and Pyglet to
build a Sphere. Additionally, we will try to attach a
Camera to the Windows which we can control with some
basic keys, or maybe even with the mouse (depending on
complexity).

A 2D atmospheric texture is generated at startup and stored.
This is then used to shade the planet sphere with simple lighting.

The mouse can be used to rotate the planet axis. Notice the
pinching distortion near the poles due to the texture wrapping.
Utilizes the shader noise functions to generate some clouds.

Note: this file is only for testing and prototyping
Requirements: Ppyglet 1.1+, ctypes and Noise by Casey Duncan

Link for Noise: https://github.com/caseman/noise.git
"""

import os
from math import cos
from math import sin
import pyglet
from pyglet.gl import *
import ctypes
from noise.shader_noise import ShaderNoiseTexture, shader_noise_glsl
from noise import shader

__author__ = "Daniel Melichar"
__copyright__ = "Copyright 2015"
__credits__ = ["Daniel Melichar", "Sarah Kreutzer"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Daniel Melichar"
__email__ = "dmelichar@student.tgm.ac.at"
__status__ = "Deployed"



### The following code is writen in the OpenGL Shading Langauge (GLSL)

vert_shader = shader.VertexShader('vertex', '''
	/* simple vertex shader that stores the vertex position, normal
	 * lighting vector and color in varyings for easy access by the
	 * frag shader
	 */

	uniform float scale;
	varying vec3 position;
	varying vec3 normal;
	varying vec3 lightvec;
	varying vec4 color;

	void main(void) {
		position = gl_Vertex.xyz * scale;
		normal = gl_NormalMatrix * gl_Normal;
		gl_Position = ftransform();
		/* Directional light assumed */
		vec4 v = gl_ModelViewMatrix * gl_Vertex;
		lightvec = gl_LightSource[0].position.xyz - v.xyz;
		color = gl_Color;
	}
''')

atmosphere_frag_shader = shader.FragmentShader('atmosphere', shader_noise_glsl + '''
	/* Animated atmospheric shader */

	uniform float time;
	varying vec3 position;
	varying vec3 normal;
	varying vec3 lightvec;
	varying vec4 color;

	void main(void) {
		float t = fbmnoise(position * 2.0 + time * 0.001, 2);
		vec3 turb = vec3(sin(t * 0.5), cos(t), 0) * 0.04;
		float h = fbmturbulence(turb + position * 0.5 + time * 0.002, 6) * 1.35;
		h = h*h;
		/* Calculate the lighting */
		vec3 N = normalize(normal);
		float intensity = max(0.0, dot(N, normalize(lightvec)));
		float glare = max(0.0, dot(N, normalize(gl_LightSource[0].halfVector.xyz)));
		vec4 ambient = gl_LightSource[0].ambient;
		vec4 diffuse = gl_LightSource[0].diffuse * intensity;
		vec4 specular = gl_LightSource[0].specular * pow(glare, 64.0);
		gl_FragColor = (ambient + diffuse + specular) * color * h;
	}
''')

atmosphere_prog = shader.ShaderProgram(vert_shader, atmosphere_frag_shader)
atmosphere_prog.install()
atmosphere_prog.uset1F('scale', 0.3)


if __name__ == '__main__':
    global xrot, yrot, d
    win = pyglet.window.Window(width=1240, height=1240, resizable=True, visible=False,
                               config=pyglet.gl.Config(sample_buffers=1, samples=4, double_buffer=True, depth_size=24))

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    fourfv = ctypes.c_float * 4
    glLightfv(GL_LIGHT0, GL_POSITION, fourfv(1, 0, 1.0, 0.5))
    glLightfv(GL_LIGHT0, GL_AMBIENT, fourfv(0.001, 0.001, 0.001, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, fourfv(2.0, 2.0, 2.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, fourfv(0.001, 0.001, 0.001, 1.0))
    glEnable(GL_COLOR_MATERIAL)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    noisetex = ShaderNoiseTexture()
    noisetex.load()

    earth_texture = pyglet.image.load(
        os.path.join(os.path.dirname(__file__), '..', '..', 'res', 'textures', 'earth.jpg')).get_mipmapped_texture()
    glTexParameteri(earth_texture.target, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(earth_texture.target, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(earth_texture.target, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(earth_texture.target, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(earth_texture.target)

    earth = gluNewQuadric()
    gluQuadricNormals(earth, GLU_SMOOTH)
    gluQuadricTexture(earth, GL_TRUE)
    glEnable(GL_CULL_FACE)
    glColor4f(1, 1, 1, 1)

    atmosphere_depth = 0.01
    atmosphere_speed = 0.85

    yrot = spin = 0.0
    xrot = -90.0
    time = 0
    posx = 0.5
    posy = 0.5
    counterForEarth = 0


    def on_resize(width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(20, 1.0 * width / height, 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


    win.on_resize = on_resize


    @win.event
    def on_mouse_motion(x, y, dx, dy):
        global xrot, yrot
        yrot += dx * 0.3
        xrot += dy * 0.3


    @win.event
    def on_draw():
        global xrot, yrot
        win.clear()

        # Sphere with Earth Texture
        glLoadIdentity()
        glTranslatef(0, 0, -4.5)
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
        glRotatef(spin, 0.0, 0.0, 1.0)
        glDisable(GL_TEXTURE_3D)
        glEnable(earth_texture.target)
        glDisable(GL_BLEND)
        gluSphere(earth, 0.45, 60, 60)

        # Sphere with Earth atmosphere
        glLoadIdentity()
        glTranslatef(0, 0, -4.5)
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
        glRotatef(spin * atmosphere_speed, 0.0, 0.0, 1.0)
        glDisable(earth_texture.target)
        noisetex.enable()
        glEnable(GL_BLEND)
        atmosphere_prog.install()
        atmosphere_prog.uset1F('time', time)
        gluSphere(earth, 0.45 + atmosphere_depth, 20, 20)
        atmosphere_prog.uninstall()


        # Sphere with Earth Texture
        glLoadIdentity()
        glTranslatef(posx, posy, -4.5)
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
        glRotatef(spin, 0.0, 0.0, 1.0)
        glDisable(GL_TEXTURE_3D)
        glEnable(earth_texture.target)
        glDisable(GL_BLEND)
        gluSphere(earth, 0.1, 60, 60)

        # Sphere with Earth atmosphere
        glLoadIdentity()
        glTranslatef(posx, posy, -4.5)
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
        glRotatef(spin * atmosphere_speed, 0.0, 0.0, 1.0)
        glDisable(earth_texture.target)
        noisetex.enable()
        glEnable(GL_BLEND)
        atmosphere_prog.install()
        atmosphere_prog.uset1F('time', time)
        gluSphere(earth, 0.1 + atmosphere_depth, 20, 20)
        atmosphere_prog.uninstall()


    def update(dt):
        global spin, time, posx, posy, counterForEarth
        spin += dt * 3.0
        time += dt

        DEG2RAD = 3.14159/180.0

        if counterForEarth>359:
            counterForEarth = 0
        else:
            counterForEarth += 1

        posx = cos(counterForEarth*DEG2RAD)*0.5
        posy = sin(counterForEarth*DEG2RAD)*0.3
       # print(posx)
       # print(posy)
        print(counterForEarth)

    pyglet.clock.schedule_interval(update, 1.0 / 30.0)

    win.set_visible()
    win.set_exclusive_mouse()
    pyglet.app.run()
