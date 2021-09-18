my_list = []
lol = open('lol.txt', 'w')
while 1 == 1:
    line = input('Ваш текст: ')
    if line == '':
        break
    else:
        lol.write(line + '\n')
lol.close()
