def div(*args):
    arg1 = int(input('Делимое: '))
    arg2 = int(input('Делитель: '))
    if arg1 == 0 or arg2 == 0:
        return 'Ноль - нельзя'
    else:
        return arg1 / arg2
print('Итог: ', div())
