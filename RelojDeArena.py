import os
import random


class Reloj():

    def __init__(self, matriz):
        self.pos_x = 0
        self.pos_y = 0
        self.matriz = []
        self.suma_reloj = 0

    def mover_derecha(self):
        y = len(self.matriz)
        x = len(self.matriz[0])

        if (self.pos_x + 3) + 1 <= x:
            self.pos_x = self.pos_x + 1
        else:
            if (self.pos_y + 3) + 1 <= y:
                self.pos_y = self.pos_y + 1
                self.pos_x = 0
        print(" ")

    def generar_matriz(self, n, m):
        for i in range(n):
            self.matriz.append([])
            for j in range(m):
                self.matriz[i].append(random.randint(0, 100))

    def obtener_reloj_actual(self):
        output = ""

        x = self.pos_x
        suma_reloj = 0

        for y in range(3):
            for x in range(3):
                suma_reloj += self.matriz[self.pos_y + y][self.pos_x + x]
                output += str(self.matriz[self.pos_y + y][self.pos_x + x]) + " "
            print(output)
            output = ""

        if suma_reloj > self.suma_reloj:
            self.suma_reloj = suma_reloj


reloj = Reloj([])
reloj.generar_matriz(5, 5)

for i in range(len(reloj.matriz)):
    print(reloj.matriz[i])

print("  ")

reloj.obtener_reloj_actual()
reloj.mover_derecha()
reloj.obtener_reloj_actual()
reloj.mover_derecha()
reloj.obtener_reloj_actual()
reloj.mover_derecha()
reloj.obtener_reloj_actual()
reloj.mover_derecha()
reloj.obtener_reloj_actual()
print("suma mayor: "+ str(reloj.suma_reloj))