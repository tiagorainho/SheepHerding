from __future__ import annotations
from states.fsm import FSM, State, Transition
from random import randint
from classes.vector import Vector

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

    def update(self, ant):
        self.current.update(ant)


class Graze(State):

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, sheep):
        # search in a random direction for green pastor
        vector = Vector(randint(-1, 1), randint(-1, 1))

        sheep.accelerate(vector = vector)

class Herd(State):

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, sheep):
        sheep.accelerate(sheep.boid_acceleration())