from itertools import count
from itertools import cycle


for el in count(int(input('Начальное число: '))):
    print(el)
    if el > 10000:
        break

my_list = ['Lol', 'Kek', 'Prikol', 12309, 0]
ct = 0
for el in cycle(my_list):
    print(el)
    if ct > 50:
        break
    ct += 1