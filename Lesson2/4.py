sr = input('Введите строку: ')
a = sr.split(' ')
ct = 1
for i in a:
    if len(i) > 10:
        i = i[0:10]
    print(f'{ct} - {i}')
    ct += 1
