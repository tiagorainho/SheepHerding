import pygame

from typing import Tuple, List

from commands.command import Command
from commands.update_dog_commands import UpdateRight, UpdateDown, UpdateLeft, UpdateUp
from commands.move_dog import MoveDog

from utils.math.vector import Vector

DOG_COMMANDS = {
    pygame.K_w: UpdateUp,
    pygame.K_s: UpdateDown,
    pygame.K_a: UpdateLeft,
    pygame.K_d: UpdateRight
}

KEY_BACK = pygame.K_z

KEY_DIRECTION = {
    pygame.K_UP: Vector(0, -1),
    pygame.K_DOWN: Vector(0, 1),
    pygame.K_LEFT: Vector(-1, 0),
    pygame.K_RIGHT: Vector(1, 0),
}

class InputHandler:

    last_commands: List[Command]

    def __init__(self, game) -> None:
        self.game = game
        self.last_commands = []

    def handle_input(self, events) -> Tuple[List[Command], List[Command]]:
        """
        Returns:
            - list of commands
            - list of commands to undo
        """

        commands = []
        commands_undo = []
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in DOG_COMMANDS:
                    command = DOG_COMMANDS[event.key]()
                    commands.append(command)

                if event.key == KEY_BACK:
                    if len(self.last_commands) == 0: continue
                    commands_undo = self.last_commands.pop()
        
        if commands:
            self.last_commands.append(commands)
        

        # controll selected dog
        keys = pygame.key.get_pressed()
        direction = Vector(0,0)
        for key, vector in KEY_DIRECTION.items():
            if keys[key]:
                direction.sum(vector)
        direction.normalize()
        command = MoveDog(direction)
        commands.append(command)

        return commands, commands_undo