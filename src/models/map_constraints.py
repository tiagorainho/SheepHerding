
from classes.vector import Vector

BORDER_REPULSIVE_FORCE: float = 1
BORDER_MARGIN: float = 5

class MapConstraints:
    border_repulsive_force: float
    border_margin: float
    game_grid: Vector

    def __init__(self,
        game_grid: Vector,
        border_repulsive_force: float = BORDER_REPULSIVE_FORCE,
        border_margin: float = BORDER_MARGIN
    ) -> None:
        self.game_grid = game_grid
        self.border_margin = border_margin
        self.border_repulsive_force = border_repulsive_force
    
    def add_repulsive_force(self, obj , direction: Vector, repulsive_force):
        mag = direction.magnitude
        acceleration = direction.div(mag*mag).limit(repulsive_force)
        obj.position.sum(acceleration)
    
    def constrain_object(self, obj):

        # fix x axis
        if obj.position.x >= self.game_grid.x - self.border_margin:
            self.add_repulsive_force(obj, Vector(x = - abs(self.game_grid.x - obj.position.x), y = 0), repulsive_force=self.border_repulsive_force)

            if obj.position.x > self.game_grid.x:
                obj.position.x = self.game_grid.x

        if obj.position.x < self.border_margin:
            self.add_repulsive_force(obj, Vector(x = abs(obj.position.x), y = 0), repulsive_force=self.border_repulsive_force)

            if obj.position.x < 0:
                obj.position.x = 0
        
        # fix y axis
        if obj.position.y >= self.game_grid.y - self.border_margin:
            self.add_repulsive_force(obj, Vector(x = 0, y = - abs(self.game_grid.y - obj.position.y)), repulsive_force=self.border_repulsive_force)

            if obj.position.y > self.game_grid.y:
                obj.position.y = self.game_grid.y

        if obj.position.y < self.border_margin:
            self.add_repulsive_force(obj, Vector(x = 0, y = abs(obj.position.y)), repulsive_force=self.border_repulsive_force)

            if obj.position.y < 0:
                obj.position.y = 0

    def update(self, objects):
        for obj in objects:
            self.constrain_object(obj=obj)