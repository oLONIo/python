test3 = open('test3.txt', 'r', encoding = 'utf-8')
sred = [0, 0]
print('Оклад менее 20к у сотрудников с фамилиями: ', end='')
for line in test3:
    splitter = line.split(' ')
    if float(splitter[1]) < 20000:
        print(splitter[0])
    sred[0] += 1
    sred[1] += float(splitter[1])
print(f'Средний оклад: {sred[1] / sred[0]}')
test3.close()