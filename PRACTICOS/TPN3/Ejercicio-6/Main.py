import random
from Docente import Docente
from Alumno import Alumno

personas = []

for i in range(10):
    if random.randrange(0,2)==1:
        personas.append(Docente("NomDoc {}".format(i),"ApeDoc {}".format(i),"Mat {}".format(i)))
    else:
        alumno = Alumno("AlumNom {}".format(i),"AlumApe {}".format(i))
        
        for j in range(10):
            alumno.agregar_materia("Mat {}".format(j))
            if random.randrange(0,2) == 1:
                break
            
        personas.append(alumno)
        
for per in personas:
    print(per.materia())
        