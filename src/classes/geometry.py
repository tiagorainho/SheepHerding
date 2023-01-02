import numpy as np

from typing import List

from classes.vector import Vector

def circle_points(radius, number_of_points) -> List[Vector]:
    t = np.linspace(0, 2*np.pi, number_of_points, endpoint=False)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    return [Vector(x,y) for x, y in np.c_[x, y]]