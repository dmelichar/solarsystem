.. Solar System documentation master file, created by
   sphinx-quickstart on Wed Dec  9 08:45:01 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Solar System's documentation!
========================================



**Team**: Kreutzer & Melichar

**Klasse**: 5AHITM

Requirements
------------

**Pyglet** via pip

.. code-block:: python

    pip install pyglet

**Pyglet-GUI** via pip

.. code-block:: python

    pip install git+https://github.com/jorgecarleitao/pyglet-gui.git

**Noise** via pip

.. code-block:: python

    pip install noise

Aufgabenstellung
----------------

In einem Team (2) sind folgende Anforderungen zu erfüllen.

- Ein zentraler Stern
- Zumindest 2 Planeten, die sich um die eigene Achse und in elliptischen Bahnen um den Zentralstern drehen
- Ein Planet hat zumindest einen Mond, der sich zusätzlich um seinen Planeten bewegt
- Kreativität ist gefragt: Weitere Planeten, Asteroiden, Galaxien,...
- Zumindest ein Planet wird mit einer Textur belegt (Erde, Mars,... sind im Netz verfügbar)

Events
~~~~~~~
 - Mittels Maus kann die Kameraposition angepasst werden: Zumindest eine Überkopf-Sicht und parallel der Planentenbahnen
 - Da es sich um eine Animation handelt, kann diese auch gestoppt werden. Mittels Tasten kann die Geschwindigkeit gedrosselt und beschleunigt werden.
 - Mittels Mausklick kann eine Punktlichtquelle und die Textierung ein- und ausgeschaltet werden.
 - Schatten: Auch Monde und Planeten werfen Schatten.

Hinweise
~~~~~~~~
- Ein Objekt kann einfach mittels glutSolidSphere() erstellt werden.
- Die Planten werden mittels Modelkommandos bewegt: glRotate(), glTranslate()
- Die Kameraposition wird mittels gluLookAt() gesetzt
- Bedenken Sie bei der Perspektive, dass entfernte Objekte kleiner - nahe entsprechende größer darzustellen sind.
- Wichtig ist dabei auch eine möglichst glaubhafte Darstellung. gluPerspective(), glFrustum()
- Für das Einbetten einer Textur wird die Library Pillow benötigt! Die Community unterstützt Sie bei der Verwendung.

Contents:

.. toctree::
   :maxdepth: 3

   src/*


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

