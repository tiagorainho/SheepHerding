
from commands.command import Command
from classes.vector import Vector
from models.dog import Dog

class UpdateDog(Command):
    last_selected_dog: Dog

    def execute(self, game):
        self.last_selected_dog = game.dog_service.selected_dog
        self.game = game

    def undo(self):
        self.game.dog_service.select(self.last_selected_dog)


class UpdateRight(UpdateDog):
    
    def execute(self, game):
        super().execute(game)
        game.dog_service.select_dog(direction=Vector(1, 0))
    
class UpdateLeft(UpdateDog):
    
    def execute(self, game):
        super().execute(game)
        game.dog_service.select_dog(Vector(-1, 0))

class UpdateDown(UpdateDog):
    
    def execute(self, game):
        super().execute(game)
        game.dog_service.select_dog(Vector(0, 1))

class UpdateUp(UpdateDog):
    
    def execute(self, game):
        super().execute(game)
        game.dog_service.select_dog(Vector(0, -1))