from ProfesorTitular import ProfesorTitular
from ProfesorSuplente import ProfesorSuplente

titulares = []
titulares.append(ProfesorTitular("Aldana","Guittierrez",21,40,1500,10,300))
titulares.append(ProfesorTitular("Pedro","Perez",21,30,1000,4,300))
titulares.append(ProfesorTitular("Maria","Gomez",21,29,1000,15,300))

suplentes = []
suplentes.append(ProfesorSuplente("Tomas","Sosa",28,40,600))
suplentes.append(ProfesorSuplente("Lucia","Torres",28,40,700))

for titular in titulares:
    print("Nombre y Apellido {}.{}".format(titular.get_nombre(),titular.get_apellido()))
    print("Es titular? Si")
    print("Remuneracion: {}".format(titular.get_remuneracion_mensual()))
    
for suplente in suplentes:
    print("Nombre y Apellido {},{}".format(suplente.get_nombre(),suplente.get_apellido()))
    print("Es titular? No")
    print("Remuneracion:{}".format(suplente.get_remuneracion_mensual()))
