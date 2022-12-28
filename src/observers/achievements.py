from .observer import Observer
from enums.events import Event
from typing import DefaultDict
from models.corral import Corral
from collections import defaultdict


class Achievements(Observer):
    scores: DefaultDict[Corral, int]

    def __init__(self):
        self.scores = defaultdict(lambda : 0)

    @property
    def total_score(self):
        return sum(self.scores.values())

    def notify(self, entity, event: Event, **kwargs):
        if event == Event.ENTER_CORRAL:
            self.scores[kwargs["corral"]] += 1
            
    def draw(self):
        print(f"score: {self.score}")