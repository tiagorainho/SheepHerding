import cProfile
import atexit
import pstats
import io

from game.sheep_game import SheepGame

DEBUG: bool = False

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