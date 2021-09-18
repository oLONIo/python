from time import sleep


class TrafficLight:
    
    __time = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}
    __color = ''

    def running(self):
        for color, st in self._time.items():
            self._color = color
            print(f'Светофор загорелся цветом "{self._color}" на {st} секунд.')
            sleep(st)

TL = TrafficLight()
TL.running()