from Cancion import Cancion##no importaba bien la clase

#cancion = Cancion.Cancion()
#cancion.nombre = "Un velero llamado libertad"
#cancion.autor = "Jose Luis Perales"
#cancion.duracion = 222.0

cancion = Cancion("Un velero llamado libertad","Jose Luis Perales",222.0)
print(cancion.get_nombre())
print(cancion.get_autor())
print(cancion.get_duracion())
cancion.info_cancion()
#print(cancion.nombre)
#print(cancion.autor)
#cancion(cancion.duracion)
