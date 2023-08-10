class Banco:
    from Direccion import Direccion
    from Persona import Persona
    
    def __init__(self,nombre_banco,direccion,clientes):
        self.__nombre_banco = nombre_banco
        self.__direccion = direccion
        self.__clientes = clientes
        
    def get_nombre_banco(self):
        return self.__nombre_banco
    
    def agregar_cliente(self,cliente):
        self.__clientes.append(cliente)
        
    def mostrar_clientes(self):
        print(f"Clientes del banco {self.__nombre_banco}")
        for cliente in self.__clientes:
            print(cliente.imprimir_datos())  
            
   # def obtener_direccion(self): #Quizas esta al pedo eso depende creo
    #    return self.direccion.obtener_direccion() # Lo puse por si necesita solo la direccion  
    
    def obtener_datos_banco(self):
        print(f"Nombre:{self.__nombre_banco}. Direccion:{self.__direccion.obtener_direccion()}")
        
        # 
