x, y = map(int,input('Введите 2 числа: ').split(' '))
def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(x, y))
