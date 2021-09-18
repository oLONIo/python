from math import factorial
from itertools import count


def lol_kek():
    for el in count(1):
        yield factorial(el)

ct = 0
lol = lol_kek()
for i in lol:
    if ct < 15:
        print(i)
        ct += 1
    else:
        break