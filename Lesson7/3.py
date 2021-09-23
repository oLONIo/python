class Cell:

    def __init__(self, qtt):
        self.qtt = int(qtt)

    def __str__(self):
        return self.qtt * "*"

    def __add__(self, other):
        return Cell(self.qtt + other.qtt)

    def __sub__(self, other):
        return self.qtt - other.qtt if (self.qtt - other.qtt) > 0 else print('Меньше нуля((')
    
    def __mul__(self, other):
        return Cell(int(self.qtt * other.qtt))

    def __truediv__(self, other):
        return Cell(round(self.qtt // other.qtt))

    def grp(self, grp_dvd):
        row = ''
        for i in range(int(self.qtt / grp_dvd)):
            row += f'{"*" * grp_dvd}\\n'
        row += f'{"*" * (self.qtt % grp_dvd)}'
        return row

cell1 = Cell(5)
cell2 = Cell(9)
print(cell1)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1.grp(5))
print(cell2.grp(10))
print(cell1 / cell2)