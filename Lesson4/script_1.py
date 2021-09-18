def func():
    time = float(input('Выработка в часах: '))
    salary = int(input('Ставка: '))
    bonus = int(input('Премия: '))
    result = time * salary + bonus
    print(f'Заработная плата: {result}')