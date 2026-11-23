import itertools 
import random


it1 = itertools.cycle(range(2))

assert [next(it1) for _ in range(6)] == [0, 1, 0, 1, 0, 1]

def it_randomwalk():
    l  =  ["N","S","W","E"]
    while True:
        yield random.choice(l)

assert all(next(it_randomwalk()) in ("N", "E", "S", "W") for _ in range(100))
    
it3 = itertools.cycle(range(7))

assert [next(it3) for _ in range(14)] == [0, 1, 2, 3, 4, 5, 6,
                                          0, 1, 2, 3, 4, 5, 6]