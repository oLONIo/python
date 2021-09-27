class DivisionByNull:

    def __init__(self, dev1, dev2):
        self.dev1 = dev1
        self.dev2 = dev2

    @staticmethod
    def divide_by_null(dev1, dev2):
        try:
            return (f'Результат - {dev1 / dev2}')
        except:
            return (f'Нельзя делить на 0!')

print(DivisionByNull.divide_by_null(0, 1))
print(DivisionByNull.divide_by_null(1, 0))

