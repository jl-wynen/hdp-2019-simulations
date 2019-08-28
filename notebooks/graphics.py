"""
Hilfsroutinen für die Grafikausgabe.
"""


import vpython
from vpython import *


def canvas(width=512,
           height=512,
           background=vector(0.9, 0.9, 0.9),
           center=vpython.vector(0, -2, 0),
           userzoom=True):
    """
    Erstelle ein VPython Canvas mit standard Parametern.
    """

    # Erzeuge eine neue Szene, dies zeigt die Grafikausgabe unter der aktuellen Notebook Zelle.
    scene = vpython.canvas()

    # Größe der Ausgabe in Pixeln
    scene.width = width
    scene.height = height

    # Hintergrunfarbe
    scene.background = background
    # Verschiebe Zentrum
    scene.center = center
    # Erlaube zoomen?
    scene.userzoom = userzoom

    return scene
