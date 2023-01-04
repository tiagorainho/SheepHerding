from typing import List
from observers.observer import Observer

class Subject:
    """
    Used to connect an object which needs to be linked to an Observer. The desired object should extend the Subject class and call the Subject.__init__() method to initiate.
    """

    observers: List[Observer]

    def __init__(self) -> None:
        self.observers = []

    def add_observer(self, obs: Observer):
        """
        Add observer to then be notified of new events.
        """
        
        self.observers.append(obs)

    def notify(self, entity, event, **kwargs):
        """
        Entrypoint to receive the notification.
        """
        
        for obs in self.observers:
            obs.notify(entity=entity, event=event, **kwargs)