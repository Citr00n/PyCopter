# Вспомогательный скрипт

from random import randint as rnd


def randbool(r, mxr):
    t = rnd(0, mxr)
    if t < r:
        return True
    return False

def randcell(w, h):
    tw = rnd(0, w-1)
    th = rnd(0, h-1)
    return(tw, th)

# 0 - наверх
# 1 - вправо
# 2 - вниз
# 3 - налево
def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rnd(0, 3)
    dx = moves[t][0]
    dy = moves[t][1]
    return(x+dx, y+dy)