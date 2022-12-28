from typing import List
from observers.observer import Observer

class Subject:

    observers: List[Observer]

    def __init__(self) -> None:
        self.observers = []

    def add_observer(self, obs: Observer):
        self.observers.append(obs)

    def notify(self, entity, event, **kwargs):
        for obs in self.observers:
            obs.notify(entity=entity, event=event, **kwargs)
        