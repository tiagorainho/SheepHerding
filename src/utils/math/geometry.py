import numpy as np

from typing import List

from utils.math.vector import Vector

def circle_points(radius, number_of_points) -> List[Vector]:
    """
    Create *number_of_points* circular points at a *radius* distance from the center (0,0).
    """
    
    t = np.linspace(0, 2*np.pi, number_of_points, endpoint=False)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    return [Vector(x,y) for x, y in np.c_[x, y]]