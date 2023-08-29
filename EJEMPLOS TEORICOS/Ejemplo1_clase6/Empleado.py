'''
Defina una interfaz Empleado que tenga los métodos calcular_salario() y mostrar_informacion()
Desarrolle la clase EmpleadoTiempoCompleto que tiene como atributos su nombre y su sueldo anual y la 
clase EmpledoTemporal que tiene nombre, sueldo_por_hora y horas_trabajadas. Ambas deben 
implementar la interfaz.
Para probar, cree una lista de 3 empleados random e imprima su información. 
¿Qué tipo de polimorfismo sucede? ¿estático o dinámico? ¿como se podría implementar el otro tipo?
'''
#### ------------------ Interfas Formal ------------------- ###
from abc import ABC, abstractmethod
class Empleado(ABC):
    
    def __init__(self,nombre):
        self._nombre = nombre
    
    @abstractmethod
    def calcular_salario(self):
        pass
    @abstractmethod
    def mostrar_informacion(self):
        pass
    
    
    
class EmpleadoTemporal(Empleado):
    
    def __init__(self,nombre,sueldo_por_hora,horas_trabajadas):
        super().__init__(nombre)  ### queria unsar el supoer
        self.__sueldo_por_hora = sueldo_por_hora
        self.__horas_trabajadas = horas_trabajadas
        
    @abstractmethod
    def calcular_salario(self):
        sueldo = self.__sueldo_por_hora
        horas = self.__horas_trabajadas
        return (sueldo * horas)
    
    @abstractmethod
    def mostrar_informacion(self):
        return f'La informacion del empleado temporal es: Nombre {self._nombre}, y el salario es de {self.calcular_salario()}'
    
    
    

class EmpleadoTiempoCompleto(Empleado):
    
    def __init__(self,nombre,sueldo_anual):
        super().__init__(nombre)
        self.__sueldo_anual = sueldo_anual
        
    @abstractmethod    
    def calcular_salario(self):
        return (self.__sueldo_anual/12)
    
    @abstractmethod
    def mostrar_informacion(self):
        return f'La informacion del empleado es: Nombre: {self._nombre} ,Sueldo Anual: {self.__sueldo_anual} , Salario mensual {self.calcular_salario()}'
    
    
    
empleado1 = EmpleadoTiempoCompleto("Brina",120000)
empleado2 = EmpleadoTemporal("Jessica",9,1000)
print(empleado1.mostrar_informacion())
print(empleado2.mostrar_informacion())
print(empleado1.calcular_salario())