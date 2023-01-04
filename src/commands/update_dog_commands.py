from commands.command import Command
from utils.math.vector import Vector
from models.dog import Dog
from services import service_locator
from services.dog_service import DogService


class UpdateDog(Command):
    last_selected_dog: Dog

    def execute(self, direction: Vector):
        dog_service: DogService = service_locator.get_service(DogService.__name__)
        self.last_selected_dog = dog_service.selected_dog
        dog_service.select_dog(direction=direction)

    def undo(self):
        dog_service: DogService = service_locator.get_service(DogService.__name__)
        dog_service.select(self.last_selected_dog)


class UpdateRight(UpdateDog):
    
    def execute(self):
        super().execute(Vector(1, 0))
    
class UpdateLeft(UpdateDog):
    
    def execute(self):
        super().execute(Vector(-1, 0))

class UpdateDown(UpdateDog):
    
    def execute(self):
        super().execute(Vector(0, 1))

class UpdateUp(UpdateDog):
    
    def execute(self):
        super().execute(Vector(0, -1))