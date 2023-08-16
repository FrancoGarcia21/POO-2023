class Persona:
    from datetime import datetime
    
    def __init__(self,nombre,apellido,fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre
        
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
        
    def to_string(self):
        return (f"Nombre:{self.__nombre}. Apellido: {self.__apellido}. Fecha de Nacimiento:{self.__fecha_nacimiento}")
    
        
        