from game.sheep_game import SheepGame

import cProfile
import atexit
import pstats
import io

DEBUG: bool = False
pr: cProfile.Profile

def exit_handler():
    """
    Handle exit to log performance stats from the game.
    """
    
    if not DEBUG: return
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('log.txt', 'w+') as f:
        f.write(s.getvalue())

if __name__ == '__main__':

    # start the register of performance metrics
    if DEBUG:
        atexit.register(exit_handler)
        pr = cProfile.Profile()
        pr.enable()

    # create and start the simulation
    SheepGame().start()

    # process performance metrics
    if DEBUG:
        pr.disable()