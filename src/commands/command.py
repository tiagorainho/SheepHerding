
class Command:
    
    def execute(self, game):
        raise NotImplemented()
    
    def undo(self):
        pass