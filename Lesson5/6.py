dict = {}
with open('test6.txt', 'r', encoding='utf-8') as kek:
    for line in kek:
        hrs = line.replace('(', ' ').split()
        dict[hrs[0][:-1]] = sum(int(i) for i in hrs if i.isdigit())
print(dict)