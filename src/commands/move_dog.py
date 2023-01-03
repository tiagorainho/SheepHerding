
from commands.command import Command
from classes.vector import Vector
from singletons import service_locator
from services.dog_service import DogService

class MoveDog(Command):
    direction: Vector

    def __init__(self, direction: Vector) -> None:
        self.direction = direction
        
    def execute(self):
        dog_service: DogService = service_locator.get_service(DogService.__name__)
        dog_service.selected_dog.accelerate(self.direction)