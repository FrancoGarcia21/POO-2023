from Persona import Persona

persona1 = Persona("Marco","Aurelio",'1999-5-2')### la fecha de nacimiento se escribe '1992-2-3' anio , mes y dia 
persona2 = Persona("Franco","Garcia",'1849-12-2')
persona3 = Persona("Marta","Moreira",'2005-8-32')

print(persona1.to_string())
print(persona2.to_string())
print(persona3.to_string())