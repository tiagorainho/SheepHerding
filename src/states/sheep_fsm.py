from __future__ import annotations
from states.fsm import FSM, State, Transition
from random import randint
from utils.math.vector import Vector

class SheepFSM(FSM):

    def __init__(self):

        graze = Graze()
        herd = Herd()

        states = [herd, graze]
        transitions = {
            "graze": Transition(herd, graze),
            "warning": Transition(graze, herd)
        }

        super().__init__(states, transitions)

    def update(self, sheep):
        self.current.update(sheep)


class Graze(State):
    """
    DO not use !! Makes the game unplayble because the pressure from the dogs become too important.
    
    Future work: make this component less important by having a medium delay when reached a certain position simulating eating.
    """

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, sheep):
        # search in a random direction for green pastor
        vector = Vector(randint(-1, 1), randint(-1, 1))

        sheep.accelerate(vector = vector)

class Herd(State):
    """
    Provide boid behaviour for the sheeps.
    """

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, sheep):
        sheep.accelerate(sheep.boid_acceleration())