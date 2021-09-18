dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
lol = open('test4.txt', 'r')
kek = open('done4.txt', 'w')
for line in lol:
    number = line.split(" - ")
    if number[0] in dict:
        word = dict[number[0]]
        kek.write(word + ' - ' + number[1])
lol.close()
kek.close()
