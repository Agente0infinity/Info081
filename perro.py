import random
import math
class Perro:
    def __init__(self, tamaño, color, raza, ladridos):
        self.tamaño = tamaño
        self.color = color
        self.raza = raza
        self.ladridos = ladridos  

    def ladrar(self):
        cantidad=math.floor(random.randint(1,25))
        for i in range(cantidad):
            print(random.choice(self.ladridos),end= " ")
         
       

yorkshire = Perro("pequeño", "café", "yorkshire", ["guau", "bark", "wulf", "wauf"])

yorkshire.ladrar()
