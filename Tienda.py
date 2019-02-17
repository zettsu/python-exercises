from Oferta import *


class Tienda():

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.ofertas = []

    def borrar_ofertas(self):
        self.ofertas = []

    def cargar_ofertas(self, nombre):
        archivo = open(nombre, "r" )
        for read in archivo.readlines():
            oferta_input = read.split(",")
            oferta = Oferta(oferta_input[0], oferta_input[1],oferta_input[2],oferta_input[3], oferta_input[4])
            self.ofertas.append(oferta)
            # codigo, nombre, precio, precio_oferta, envio_gratis


tienda = Tienda("Tienda Inglesa", "ALgun lado")
tienda.cargar_ofertas("ofertas")
for oferta in tienda.ofertas:
    print(oferta)

