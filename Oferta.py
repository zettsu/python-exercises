import  os


class Oferta():

    def __init__(self, codigo, nombre, precio, precio_oferta, envio_gratis):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.precio_oferta = precio_oferta
        self.envio_gratis = envio_gratis

    def __str__(self):
        return "Codigo:" + str(self.codigo) + "\n" + "Nombre:" + self.nombre + "\n" + "Precio:" + str(self.precio) + "\n" + "Precio Oferta:" + str(self.precio_oferta) + "\n" + "Envio gratis:" + str(self.envio_gratis) + "\n"

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_precio(self, precio):
        self.precio = precio

    def set_oferta(self, value):
        self.envio_gratis = value

    def get_oferta(self):
        return self.precio_oferta

    def set_envio_gratis(self, value):
        self.envio_gratis = value

    def get_envio_gratis(self):
        return self.envio_gratis

    def envio_gratis(self):
        self.envio_gratis = True

    def set_envios_gratis(ofertas):
        for oferta in ofertas:
            if not oferta.get_envio_gratis() :
                oferta.envio_gratis()

    def get_envios_gratis(ofertas):
        envios_gratis = []

        for oferta in ofertas:
            if oferta.get_envio_gratis() :
                envios_gratis.append(oferta)

        return envios_gratis

    def get_descuentos_50(ofertas):
        descuentos = []

        for oferta in ofertas:
            diferencia = oferta.precio - oferta.precio_oferta
            descuento = diferencia / oferta.precio * 100
            if descuento >= 50:
                descuentos.append(oferta)

        return descuentos


oferta1 = Oferta(1,"Leche", 28, 25, False)
oferta3 = Oferta(3,"Agua Salus 5L", 80, 80, True)
oferta2 = Oferta(2,"Aromatizador Glade 2x1", 300, 120, False)

ofertas = [oferta1, oferta2, oferta3]
lista_ofertas = Oferta.get_envios_gratis(ofertas)

print("Listado de Envios gratis\n")

for ofertas_l in lista_ofertas:
    print(ofertas_l)

lista_descuentos = Oferta.get_descuentos_50(ofertas)

print("Listado de descuentos\n")

for descuento in lista_descuentos:
    print(descuento)
