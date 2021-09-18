class Road:

    _standart_weight: float = 25
    
    def __init__(self, width, length):

            self._width = float(width)
            self._length = float(length)
            
    def mass_needed(self, thickness: float):
        return self._length * self._width * self._standart_weight * thickness
    
road = Road(20, 5000)
print(f'Масса асфальта составит ~{round(road.mass_needed(0.005))} тонн.')
