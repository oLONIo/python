my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
while 1 == 1:
    i = int(input('Введите элемент рейтинга: '))
    j = 0
    if i <= my_list[len(my_list) - 1]:
        my_list.append(i)
    else:
        while i < my_list[j]:
            j += 1
        my_list.insert(j, i)
    print(my_list)
    q = input('Формирование списка завершено? (Y/N)): ')
    if q.lower() == 'y':
        break
