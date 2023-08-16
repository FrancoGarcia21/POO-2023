class Persona:
    
    def __init__(self,nombre,apellido,cuil,telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil
        self.__telefono = telefono
        
        ### hare getter y setter luego vere cuales me sirven y borro los que no
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_cuil(self):
        return self.__cuil
    
    def get_telefono(self):
        return self.__telefono
    
    # en teoria esta clase esta completa
    
