count = int(input('Количество элементов списка: '))
list1 = []
i = 0
while i < count:
    list1.append(input('Переменная: '))
    i += 1
for i in range(int(len(list1)/2)):
        list1[i], list1[i + 1] = list1 [i + 1], list1[i]
        i += 2
print(list1)
