class VideoStreaming:
    #titulo= '' No es necesario poner los atributos antes
    #descripcion = '' # de esto se encarga el constructor
    #visibilidad = ''# estaria de mas
    
    def __init__(self, titulo, descripcion, visibilidad, es_para_ninos):
        self.__titulo = titulo              #Ninguno de estos atributos cumpliando el encapsulamiento
        self.__descripcion = descripcion    #como no se herendan , solo deben quedan en privados
        self.__visibilidad = visibilidad    #
        self.__es_para_ninos = es_para_ninos#
        
    def get_titulo(self):## como estaba encapsulado necesitaba un get 
        return self.__titulo## 

class Lista:
    #lista = []#lo mismo esto debe estar definido en el construcor ## si no defino el constructor resulta
    # pero no deberia tener este atributo como publico
    def __init__(self):
        self.lista = []#Tambien debe estar en privado para no romper el encapsulamiento
# normalmente esto no deberia estar en publico 

    def agregar_video(self, video):
        self.lista.append(video)##esto deberia estar en privado , no estaba encapsulado
    
listaReproducible = Lista()
listaPrivada = Lista()

for i in range(1,10):
    listaReproducible.agregar_video(VideoStreaming("video {}".format(i), "descripcion {}".format(i),"Publico", True))
    
listaPrivada.agregar_video(VideoStreaming("video {}".format(1),"descripcion {}".format(1), "Privado", False))

Lista = listaReproducible.lista ## Verificar aca hay un error me dice que lista no es iterable
for video in listaReproducible.lista:
    print(video.get_titulo())


#listaReproducible.agregar_video(VideoStreaming("video {}".format(2), "descripcion {}".format(2),"Publico", True))
# en teoria anda