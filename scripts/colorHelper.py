import random

def randomColor():
    return tuple([random.randint(0,255) for x in [0,1,2]])