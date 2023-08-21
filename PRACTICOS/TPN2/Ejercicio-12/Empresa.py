from Persona import Persona
class Empresa:
    def __init__(self,nombre,direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empleados = []
        
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self,direccion):
        self.__direccion = direccion
        
    def agregar_empleado(self,empleado):
        self.__empleados.append(empleado)
        
    def cantidad_empleados(self):
        total_empleados = len(self.__empleados)
        print("La cantidad de empleados que tiene la empresa es: ",total_empleados)
    
    def mostrar_info_empleados(self):
        for empleado in self.__empleados:
            print(empleado.info_persona())
        
        