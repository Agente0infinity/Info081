import random
import math
import time
class Perro:
    def __init__(self, tamaño, color, raza, ladridos):
        self.tamaño = tamaño
        self.color = color
        self.raza = raza
        self.ladridos = ladridos  

    def ladrar(self):
        cantidad=math.floor(random.randint(1,1000))
        for i in range(cantidad):
            time.sleep(1)
            print(math.floor(random.choice(self.ladridos)),end= " ")
         
       

yorkshire = Perro("pequeño", "café", "yorkshire", ["guau", "bark", "wulf", "wauf"])

print(yorkshire.ladrar())
