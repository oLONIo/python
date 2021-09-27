class OnlyInt:

    def __init__(self):
        self.my_list = []

    def inpt(self):

        q = int(input('Введите значение: '))
        self.my_list.append(q)

        while True:
            try:
                q = int(input('Введите значение: '))
                self.my_list.append(q)
            except:
                print(f'Не цифра!')
                print(f'\nТекущий список: {self.my_list}\n')
                yn = input(f'Ввести ещё раз? Y/N ')

                if (yn) == 'Y' or yn == 'y':
                    print(test.inpt())
                elif yn == 'N' or yn == 'n':
                    print('Выход!')
                    exit()

test = OnlyInt()
print(test.inpt())

