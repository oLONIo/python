class Data:

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        date = day_month_year.split('-')
        return f'{[int(i) for i in date]}'

    @staticmethod
    def valid(day, month, year):
  
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Правильный год!'
                else:
                    return f'Неправильный год!'
            else:
                return f'Неправильный месяц!'
        else:
            return f'Неправильный день!'

    def __str__(self):
        return f'Текущая дата - {kek.extract(self.day_month_year)}'


kek = Data('19-12-2100')
print(Data.valid(1, 100, 2020))
print(kek.valid(9, 12, 2023))
print(Data.extract('11-11-2011'))
print(kek.extract('11-11-2020'))
print(kek)

