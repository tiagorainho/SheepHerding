from observers.observer import Observer
from enums.events import Event
from typing import DefaultDict
from models.corral import Corral
from collections import defaultdict
from singletons import service_locator
from services.sound_service import SoundService

VOLUME = 0.1

class Achievements(Observer):
    scores: DefaultDict[Corral, int]
    
    def __init__(self):
        self.scores = defaultdict(lambda : 0)

    @property
    def total_score(self):
        return sum(self.scores.values())

    def notify(self, entity, event: Event, **kwargs):
        if event == Event.ENTER_CORRAL:

            # update score
            self.scores[kwargs["corral"]] += 1

            # play sound
            service_locator.get_service(SoundService.__name__).play_win_gold(volume=VOLUME)
            
    def draw(self):
        print(f"score: {self.score}")