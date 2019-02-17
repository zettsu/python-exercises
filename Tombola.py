import os
from random import randrange


class Tombola():

    def __init__(self):
        self.jugadores = []
        self.ganadores = []

    def sortear(self):
        for i in range(1, 20):
            self.ganadores.append(randrange(1, 99))

    def revisar_jugada(self, numeros):
        aciertos = 0;

        for numero in numeros:
            try:
                if self.ganadores.index(numero):
                    aciertos += 1
            except ValueError:
                continue
        print("Cantidad de numeros/aciertos " + str(len(numeros)) + "/" + str(aciertos))
        return aciertos

    def calcular_premio(self, dinero, aciertos, numeros):
        multiplicador = 0

        if numeros == 3:
            if aciertos == 3:
                multiplicador = 60

        if numeros == 4:
            if aciertos == 3:
                multiplicador = 9
            if aciertos == 4:
                multiplicador = 180

        if numeros == 5:
            if aciertos == 3:
                multiplicador = 3
            if aciertos == 4:
                multiplicador = 24
            if aciertos == 5:
                multiplicador = 900

        if numeros == 6:
            if aciertos == 3:
                multiplicador = 1.5
            if aciertos == 4:
                multiplicador = 9
            if aciertos == 5:
                multiplicador = 90
            if aciertos == 6:
                multiplicador = 3600

        if numeros == 7:
            if aciertos == 3:
                multiplicador = 1
            if aciertos == 4:
                multiplicador = 3
            if aciertos == 5:
                multiplicador = 30
            if aciertos == 6:
                multiplicador = 600
            if aciertos == 7:
                multiplicador = 1200

        return multiplicador * dinero

    def ver_sorteados(self):
        cont = 1
        columna = ""
        for bolilla in tombola.ganadores:
            columna += str(cont) + ". " + str(bolilla) + "\t"
            cont += 1

            if cont == 6 or cont == 11 or cont == 16 or cont == 20:
                print(columna)
                columna = ""


tombola = Tombola()
tombola.sortear()

print("\n")
print("Numeros ganadores \n")

tombola.ver_sorteados()

jugada = [12, 56, 99, 89, 50, 43, 23]
print("Jugada" + str(jugada))
print("\n")
aciertos = tombola.revisar_jugada(jugada)

premio = tombola.calcular_premio(36,aciertos, len(jugada))
print("\n")
print("Premio : "+str(premio))