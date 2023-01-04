from observers.observer import Observer
from enums.events import Event
from typing import DefaultDict
from models.corral import Corral
from collections import defaultdict
from services.service_locator import ServiceLocator
from services.sound_service import SoundService

VOLUME = 0.1

class Achievements(Observer):
    scores: DefaultDict[Corral, int]
    service_locator: ServiceLocator
    
    def __init__(self):
        self.scores = defaultdict(lambda : 0)
        self.service_locator = ServiceLocator.get_instance()

    @property
    def total_score(self):
        """
        Get the total score on all corrals.
        """
        
        return sum(self.scores.values())

    def notify(self, entity, event: Event, **kwargs):
        """
        Implement the notify of the Achievements, this will listen to the ENTER_CORRAL event.
        """
        
        if event == Event.ENTER_CORRAL:

            # update score
            self.scores[kwargs["corral"]] += 1

            # play sound
            self.service_locator.get_service(SoundService.__name__).play_win_gold(volume=VOLUME)