class Censo:
    from Familia import Familia
    
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__familias = []
        
    
    def agregar_fami(self,familia):
        self.__familias.append(familia)
        
    def cantidad_fami(self):
        cantidad = len(self.__familias)
        print(f"La cantidad de familias censadas fueron: {cantidad}")
        
    def cantidad_personas(self):
        cantidad = 0
        for familia in self.__familias:
            cantidad += familia.cantidad_inte()
        print (f"La cantidad de personas censadas fueron: {cantidad}")

    def promedio_total_familias(self):
        promedio_total = 0
        suma_promedios = 0
        if not self.__familias:
            return print(f"La edad promedio es: {0}")  # Si no hay familias, el promedio total es 0
        suma_promedios = sum(familia.promedio_edad_familia() for familia in self.__familias)
        
        promedio_total = suma_promedios / len(self.__familias)
        return promedio_total
    
    def cantidad_total_trabajadores(self):
        if not self.__familias:
            return print(f"Cantidad de trabajadores: {0} ")
        total = sum(familia.cantidad_trabajadores() for familia in self.__familias)
        return print(f"Cantidad de trabajadores:{total}")
        

        
        
        
        
         #  def promedio_edad_familia(self):
        #if not self.__integrantes:
         #   return 0  # Si no hay integrantes, el promedio es 0
        #suma_edades = sum(integrante.devolver_edad() for integrante in self.__integrantes)
        #promedio = suma_edades / len(self.__integrantes)
        #return promedio