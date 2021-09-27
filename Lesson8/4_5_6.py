class MachinesStore:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.full = []
        self.store = []
        self.test = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Цена за 1 шт. устройства "{self.name}": {self.price}руб.\nВсего на складе: {self.quantity}'

    @classmethod
    def what_to_sell(self):
        try:
            test = input(f'Название устройства: ')
            test_p = int(input(f'Введите цену за шт: '))
            test_q = int(input(f'Количество: '))
            self.test = {'Модель устройства': test, 'Цена за ед': float(test_p), 'Количество': int(test_q)}
            self.store.append(self.test)
            print(f'Текущий список: {self.store}')
        except:
            return f'Странные данные!'

        yn = input(f'Продолжить? Y/N ')

        if (yn) == 'Y' or yn == 'y':
            return MachinesStore.what_to_sell(self)
        else:
            self.full.append(self.store)
            print(f'Весь склад:\n{self.full}')
            return f'Выход!'


class Printer(MachinesStore):
    def printer(self):
        return f'Сколько может напечатать принтер {self.name}: {self.numb}'

class Scanner(MachinesStore):
    def scanner(self):
        return f'Сколько может отсканировать {self.name}: {self.numb}'

class Copier(MachinesStore):
    def copier(self):
        return f'Сколько может копировать {self.name}: {self.numb}'


test_1 = Printer('cherry', 35000, 134, 1000000)
test_2 = Scanner('lada', 1000, 4, 1)
test_3 = Copier('sumsang', 50000, 2, 9999999)
print(test_1.what_to_sell())
print(test_2.what_to_sell())
print(test_3.what_to_sell())
print(test_1.printer())
print(test_2.scanner())
print(test_3.copier())