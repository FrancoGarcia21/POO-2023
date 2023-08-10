class Direccion:
    def __init__(self,calle,numero,ciudad):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        #En teoria esta clase esta bien / Parece que mi error se encuentra en las otras clases que lo componen
    def obtener_direccion(self):
        return f"{self.calle} {self.numero} , {self.ciudad}"