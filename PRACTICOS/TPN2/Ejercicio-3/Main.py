from Alumno import Alumno

alumno1 = Alumno()
alumno1.iniciar()## esta mal usarlo asi pero supuestamente no debo cambiar la clase main
#print(f'{alumno1.getNombreYapellido()}{" DNI: "}{alumno1.getDni()}')### borrar esto
alumno1.setNombre("Alejandro")
alumno1.setApellido("Rojas")
alumno1.setDni(111111111) #### hasta aca anda joya 
alumno2 = Alumno() ##en teoria no deberia agregar esto pero luego pregunto
alumno2.iniciar_con_nom_ape("Martin","Rosales")##esto tambien lo cambie
###print(alumno2.getNombre())#esto lo agregue para probar anda el getter
alumno2.setDni(111111122)
print(f'{alumno1.getNombreYapellido()}{" DNI: "}{alumno1.getDni()}')
print(f'{alumno2.getNombreYapellido()}{" DNI:"}{alumno2.getDni()}')
###################print(alumno2.getNombre())