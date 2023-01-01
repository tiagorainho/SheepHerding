import pygame

from typing import Tuple, List

from commands.command import Command
from commands.update_dog_commands import UpdateRight, UpdateDown, UpdateLeft, UpdateUp

KEY_DIRECTION = {
    pygame.K_w: UpdateUp,
    pygame.K_s: UpdateDown,
    pygame.K_a: UpdateLeft,
    pygame.K_d: UpdateRight
}

KEY_BACK = pygame.K_z

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
                if event.key in KEY_DIRECTION:
                    command = KEY_DIRECTION[event.key]()
                    commands.append(command)

                if event.key == KEY_BACK:
                    if len(self.last_commands) == 0: continue
                    commands_undo = self.last_commands[-1]
        
        self.last_commands.append(commands)
        
        return commands, commands_undo
        