line = input('Введите цифры через пробел: ')
line = line[:27]
with open('test5.txt', 'w+') as kek:
    kek.writelines(line)
    line = line.split(' ')
print(sum(map(int, line)))
