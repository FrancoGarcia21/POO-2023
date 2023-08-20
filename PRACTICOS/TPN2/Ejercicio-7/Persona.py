from datetime import datetime,date
class Persona:
    
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
        
    def get_apellido(self):
        return self.__fecha_nacimiento
        
    def to_string(self):
        return (f"Nombre:{self.__nombre}. Apellido: {self.__apellido}. Fecha de Nacimiento:{self.__fecha_nacimiento}")
    
    
    
    def devolver_edad(self):
        hoy = datetime.today().year
        fecha = datetime.strptime(self.__fecha_nacimiento,'%Y-%m-%d')
        edad = hoy - fecha.year
        return (f"Edad: {edad}")