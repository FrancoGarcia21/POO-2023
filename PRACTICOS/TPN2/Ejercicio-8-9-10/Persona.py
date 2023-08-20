from datetime import datetime,date
class Persona:
    
    def __init__(self,nombre,apellido,fecha_nacimiento,sexo,estudia,trabaja):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__sexo = sexo
        self.__estudia = estudia
        self.__trabaja = trabaja
        
    def devolver_edad(self):
        hoy = datetime.today().year
        fecha = datetime.strptime(self.__fecha_nacimiento,'%Y-%m-%d')
        edad = hoy - fecha.year
        return edad   
        
        
    def info_persona(self):
        return (f"Nombre: {self.__nombre}. Apellido: {self.__apellido}. Edad: {self.devolver_edad()}. Sexo {self.__sexo}. Trabaja: {self.__trabaja}. Estudia: {self.__estudia}")
    
    def get_trabaja(self):
        return self.__trabaja
    
    def puede_trabajar(persona):
        if persona.devolver_edad() > 18:
            return (f"La persona puede trabajar")
        else:
            return (f"La persona no puede trabajar")
        
    def puede_manejar(persona):
        if persona.devolver_edad() > 16:
            return (f"La persona puede manejar")
        else:
            return (f"La persona no puede manejar")