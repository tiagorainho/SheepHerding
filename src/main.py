from game.sheep_game import SheepGame

import cProfile

DEBUG: bool = False

import atexit
import pstats
import io

pr: cProfile.Profile

def exit_handler():
    if not DEBUG: return
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('log.txt', 'w+') as f:
        f.write(s.getvalue())

if __name__ == '__main__':

    if DEBUG:
        atexit.register(exit_handler)
        pr = cProfile.Profile()
        pr.enable()

    # create and start the simulation
    SheepGame().start()

    if DEBUG:
        pr.disable()