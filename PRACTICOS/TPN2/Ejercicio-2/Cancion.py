class Cancion:
    def __init__(self,nombre,autor,duracion):##la clase no tenia constructori y tampoco estbaan en privado los atributos
        self.__nombre = nombre
        self.__autor = autor
        self.__duracion = duracion
        
    def get_nombre(self): ## hice los getters
        return self.__nombre
    
    def get_autor(self):
        return self.__autor
    
    def get_duracion(self):
        return self.__duracion
    
    def info_cancion(self):
        print(f"Nombre de la Cancion: {self.__nombre}. Nombre del Autor: {self.__autor}.Duracion de la cancion: {self.__duracion}")
        

