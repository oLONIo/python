class Car:

    def __init__(self, speed, color, name, is_police):

        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        return f'{self.name} поехала!'
    
    def stop(self):
        self.speed = 0
        return f'{self.name} остановилась('
    
    def turn(self, direction: str):
        self._direction = direction

        if direction == 'right':
            return f'{self.name} повернула направо!!!'
        else:
            return f'{self.name} повернула налево!!!'

    def police(self):

        if self.is_police == True:
            return f'{self.name} едет!!! Шухер!!'
        else:
            return f'{self.name} - вовсе не полиция, ложная тревога...'

class TownCar(Car):

    def show_speed(self):
        return f'Скорость городской машины - {self.speed} км/ч.'

        if self.speed > 40:
            return f'Скорость "{self.name}" выше положенной!!!'

class SportCar(Car):
    
    def show_speed(self):
        return f'Спорткар летит по городу со скоростью {self.speed} км/ч!'

class WorkCar(Car):

    def show_speed(self):
        print(f'Скорость рабочей машины - {self.speed} км/ч.')

        if self.speed > 60:
            print(f'Скорость {self.name} выше положенной!!!')

class PoliceCar(Car):

    def police(self):

        if self.is_police == True:
            return f'{self.name} едет!!! Шухер!!'
        else:
            return f'{self.name} - не полиция в итоге, ложная тревога...'
    
    def show_speed(self):
        return f'Скорость {self.name} - {self.speed} км/ч'

r = 'right'
l = 'left'

regera = SportCar(210, 'Серый', 'regera', False)
cherry = TownCar(30, 'Красный', 'cherry', False)
lastochka = WorkCar(144, 'Черный', 'lastochka', True)
mersedes = PoliceCar(347, 'Синий',  'mersedes', True)
print(f'{lastochka.go(144)} со скоростью {lastochka.show_speed()}')
print(f'Вдруг {cherry.turn(r)} и подрезала машину, поэтому {regera.stop()}')
print(lastochka.turn(l))
print(f'Цвет {lastochka.name} - {lastochka.color}')
print(f'Присмотревшись к {regera.name}, понятно, что {regera.police()}')
print(f'Присмотревшись к {lastochka.name}, понятно, что {lastochka.police()}')
print(regera.show_speed())
print(cherry.show_speed())
print(mersedes.police())
print(mersedes.show_speed())


#Не понимаю почему в 4 задании без значения в скобках не работает 73 строчка кода lastochka.go(144) 
#И выводит в консоль зачем-то целый класс WorkerCar и все команды, 
#которые там написаны вместо одной lastochka.go()... 