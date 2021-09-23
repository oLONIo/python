class Wear:

    _all = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self._all.append(self.size)

    @property
    def full(self):
        return f'Всего такни надо - ~{round(self._all[0] / 6.5 + 0.5) + round(self._all[1] * 2 + 0.3)}'
        

class Coat(Wear):

    def __str__(self):
        return f'Надо ткани на "{self.name}" - ~{round(self.size / 6.5 + 0.5)}'
        
class Costume(Wear):

    def __str__(self):
        return f'Надо ткани на "{self.name}" - ~{round(self.size * 2 + 0.3)}'

coat = Coat('Коат от кутюр', 7)
costume = Costume('Шыкарный кастюм от Лоу Ватон', 3)
print(costume.full)
print(coat)
print(costume)