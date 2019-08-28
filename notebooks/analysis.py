"""
Routinen zur Auswertung der Simulationen.
"""


from vpython import acos, dot, pi, vector


def angle_between(v1, v2):
    """
    Berechne den Winkel zwischen zwei Vektoren.
    Das Ergebnis ist in Grad.
    """
    return acos(dot(v1, v2) / (v1.mag * v2.mag)) * 180.0 / pi


def angles(vectors, ref=vector(0, 1, 0)):
    """
    Berechne den Winkel zwischen allen Vektoren in vectors und dem Referenzvektor.
    """
    return [angle_between(vec, ref) for vec in vectors]
