from Persona import Persona
class Familia:
    
    def __init__(self):
        self.__integrantes = []
        
    def agregrar_integrante(self,persona):
        self.__integrantes.append(persona)
        
        
    def mostrar_integrantes(self): 
        for integrante in self.__integrantes:
            print(integrante.info_persona())
            
    def cantidad_inte(self):
        cantidad_integrantes = len(self.__integrantes)
        return cantidad_integrantes
    
    def promedio_edad_familia(self):
        if not self.__integrantes:
            return 0  # Si no hay integrantes, el promedio es 0
        suma_edades = sum(integrante.devolver_edad() for integrante in self.__integrantes)
        promedio = suma_edades / len(self.__integrantes)
        return promedio
    
    def cantidad_trabajadores(self):
        trabajadores = sum(1 for persona in self.__integrantes if persona.get_trabaja())
        return trabajadores
