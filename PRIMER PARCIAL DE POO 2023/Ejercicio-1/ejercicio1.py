"""
Clases:

    Articulo:
        tipo_articulo
        nombre_articulo
        fecha_caducidad
        precio_articulo
        dosis
        -------------------
        mostrar_atributos()
        
    Venta:
        
        nro_venta
        fecha_venta
        valor_venta
        lista_articulos[]
        ------------
        calcular_valor_Venta()
        
    Ticket:
        nro_ticket
        historial = []
        -------------
        imprimir_ticket()
        agregar_a_historial()

"""
class Articulo:
    
    def __init__(self,nombre_articulo,tipo_articulo,fecha_caducidad,precio_articulo,dosis):
        self.__nombre_articulo = nombre_articulo
        self.__tipo_articulo = tipo_articulo
        self.__fecha_caducidad = fecha_caducidad
        self.__precio_articulo = precio_articulo
        self.__dosis = dosis
        
    def mostrar_atributos():
        pass# haria un to_string
    
    
class Venta:
    
    def __init__(self,nro_venta,fecha_venta):
        self.__nro_venta = nro_venta
        self.__fecha_venta =fecha_venta
        self.__lista_articulos= []
        
    def agregar_articulo(articulo):
        pass # aca agregaria el articulo a la lista 
    
    def calcular_Valor_venta():
        pass # aca haria el caluculo de todos los elementos que estan en la lista de articulos
    
class Ticket:
    
    def __init__(self,nro_ticket,):
        self.__nro_ticket = nro_ticket
        
    ## esta clase importaria los elementos de la clase Venta y Articulo 
    #haria los calculos y mostraria el ticket final
    
    def imprimir_ticket():
        pass
    
    def agregar_historial():
        pass
    