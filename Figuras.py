class Figura():
    def __init__(self):
        pass
    def calc_area(self):
        pass
    def calc_perimetro(self):
        pass
        
class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    def calc_area(self):
        return self.base *self.altura
    def calc_perimetro(self):
        return 2*(self.base + self.altura)
        
import math

class Circulo(Figura):
    def __init__(self,radio):
        super().__init__()
        self.radio = radio
    def calc_area(self):
        return math.pi * self.radio **2
    def calc_perimetro(self):
        return math.pi * 2 * self.radio

c1 = Rectangulo(3, 4)
c2 = Circulo(5)
print(c1.calc_area(), c1.calc_perimetro())
print(c2.calc_area(), c2.calc_perimetro())
