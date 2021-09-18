with open('test2.txt') as test2:
    ct_lines = 0
    ct_words = []
    for line in test2:
        ct_lines += 1
        ct_words.append(len(line.split(' ')))
    print('Всего строк: ', ct_lines)
    for i in range(len(ct_words)):
        print(f'Слов в {i+1} строке - {ct_words[i]}')
