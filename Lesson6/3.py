class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: float = 0, bonus: float = 0):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


all_info = Position('Kek', 'Ivanovich', 'Cooker', 10000, 10)

print(all_info.get_full_name())
print(all_info.position)
print(all_info.get_total_income())