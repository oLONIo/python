w = input('Вводите до остановки символом "q": ')
w = w.split(' ')
def func(w):
    sm = 0
    while 1 == 1:
        for j in range(0, len(w)):
            if w[j] == 'q':
                print('Сумма:', sm)
                exit(0)
            else:
                sm += int(w[int(j)])
        print('Сумма:', sm)
        w = input('Вводите до остановки символом "q": ')
        w = w.split(' ')
print('Сумма:', func(w))
