''''
Tengo que alterar el metodo descripcion para que este en las 3 clases 
'''

class TecnicaArtistica:
    def __init__(self, tecnica,porcen_tec): # agregar un atributo que sea un porcentaje para poder calcular el precio
        self._tecnica = tecnica
        self._porcen_tec = porcen_tec

    def descripcion(self):## debo reformar esta funcion para utilizarla mejor
        return f"Tecnica: {self._tecnica}. Porcentaje de la Tecnica Artistica: {self._porcen_tec}"

class EstiloArtistico:
    def __init__(self, estilo,porcen_esti):## ategue atributo procenEsti que es el porcentaje del valor extra  
        self._estilo = estilo## acordate todo debe estar en protected que es un solo guion _
        self._porcen_esti = porcen_esti

    def descripcion(self):## debo reformar esta funcion para utilizarla con el mismo nombre en todas las clases
        return f"Estilo: {self._estilo}. Porcentaje del Estilo Artistico: {self._porcen_esti}"

class ObraDeArte(TecnicaArtistica, EstiloArtistico):
    def __init__(self, tecnica, porcen_tec, estilo, porcen_esti, titulo, precio_base):
        TecnicaArtistica.__init__(self, tecnica , porcen_tec)
        EstiloArtistico.__init__(self, estilo , porcen_esti)
        self._titulo = titulo
        self._precio_base = precio_base

    def mostrar_info(self):
        print(f"Titulo: {self._titulo}")
        #print(super().descripcion())### Al usar el super voy a utilizar el metodo del padre que primero heredo, con esto lo va hacer una sola vez
        print(TecnicaArtistica.descripcion(self))# Al especifcar de que clase quiero que utilize el metodo
        print(EstiloArtistico.descripcion(self))# Lo mismo que arriba si heredo de dos clases paadres , y tengo metodos con el mismo nombre
        #tengo que especificarle a Python cual es el que tiene que usar , si no usa el primero que heredo 
        print(f"Precio base: ${self._precio_base:.2f}")

    def calcular_costo(self):
        costo_tecnica = self._porcen_tec
        costo_estilo = self._porcen_esti
        return (self._precio_base + (self._precio_base * costo_tecnica) + (self._precio_base * costo_estilo))


obra = ObraDeArte("Pintura al óleo",0.20,"Impresionismo",0.10,"Impression, soleil levant",500)
## tenia mal la instanciacion del objeto
obra.mostrar_info()
print(f"Costo calculado: ${obra.calcular_costo():.2f}")
obra2 = ObraDeArte("Escultura",0.60,"Renacimiento",0.10,"David",1500)
# tenia mal la instancion del objeto
obra2.mostrar_info()
print(f"Costo calculado: ${obra2.calcular_costo():.2f}")