class Alumno:
    
    def __init__(self):# esto esta rarisimo
        self.__nombre = "" #quiero hacer que el objeto este vacio
        self.__apellido = ""# pero veo raro el init
        self.__dni = ""
        
        
    def iniciar(self): #supuse que iniciar es setear el objeto en vacio todo sus atributos
        self.__nombre = input("Ingrese el nombre del alumno: ")
        self.__apellido = input("Ingrese el apellido del alumno: ")
        self.__dni = int(input("Ingrese el DNI del alumno: "))
    
    def iniciar_con_nom_ape(self,nombre,apellido):
        #alumno = cls() #fijate como sobrecargar el constructor
        self.__nombre = nombre
        self.__apellido = apellido
        
    #para probar algo
    def getNombre(self):
        return self.__nombre
        
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setApellido(self,apellido):
        self.__apellido = apellido
    
    def setDni(self,dni):
        self.__dni = dni
        
    def getDni(self):
        return self.__dni
    
    def getNombreYapellido(self):
        return f'Nombre: {self.__nombre}. Apellido: {self.__apellido}'                              #self.__nombre, self.__apellido
    
            
        
            