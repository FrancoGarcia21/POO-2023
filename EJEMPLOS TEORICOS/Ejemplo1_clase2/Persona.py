class Persona:
    from Direccion import Direccion
    
    def __init__(self,nombre,dni,direccion):
        self.__nombre = nombre
        self.__dni = dni
        self.__direccion = direccion
        
    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def imprimir_datos(self):#Seria el to_string de java si no me equivoco
        print(f"Nombre: {self.__nombre}. DNI: {self.__dni}. Direccion {self.__direccion.obtener_direccion()}")## aca deberia usar la funcion que hice en direccion
        #pero tengo que ver si esta correcto
    
#operetor f en python buscar
# print(f"Retira {monto}. Nuevo saldo: {self.saldo}")