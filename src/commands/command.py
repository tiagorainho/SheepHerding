
class Command:
    
    def execute(self, game):
        raise NotImplementedError()
    
    def undo(self):
        pass