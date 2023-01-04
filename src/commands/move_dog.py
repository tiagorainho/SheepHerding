
from commands.command import Command
from utils.math.vector import Vector
from services.service_locator import ServiceLocator
from services.dog_service import DogService

class MoveDog(Command):
    direction: Vector

    def __init__(self, direction: Vector) -> None:
        self.direction = direction
        
    def execute(self):
        service_locator = ServiceLocator.get_instance()
        dog_service: DogService = service_locator.get_service(DogService.__name__)
        dog_service.selected_dog.accelerate(self.direction)