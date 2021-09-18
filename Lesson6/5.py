class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen:
    title = 'Ручка'

    def draw(self):
        print(f'{self.title} начала писать.')

class Pencil:
    title = 'Карандаш'

    def draw(self):
        print(f'{self.title} начал чертить.')


class Handle:
    title = 'Маркер'

    def draw(self):
        print(f'{self.title} начал рисовать.')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()

