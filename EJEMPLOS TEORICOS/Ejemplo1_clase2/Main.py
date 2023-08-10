from Persona import Persona
from Direccion import Direccion
from CuentaCorriente import CuentaCorriente
from Banco import Banco

dirban = Direccion("San Martin",1200,"Comodoro Rivadavia")
dir1 = Direccion("O'Higgins",780,"Comodoro Rivadavia")
persona1 = Persona("Franco Garcia",3943720,dir1)
persona2 = Persona("Raul Guittierres",32039203,dir1)

print(dir1.obtener_direccion()) ## Bien el metodo obtener direccion me lo devulve sin problemas
print(dirban.obtener_direccion())## Bien funciona en las dos
persona1.imprimir_datos()##Bien anda la funcion imprimir_datos / Pero me sigue tirando none 
#no se de donde sale 


banco1 = Banco("Galicia",dir1,[])#en toeria el banco se esta instanciando de manera normal
banco1.obtener_datos_banco() #Me tira los datos del banco FUNCIONA
banco1.agregar_cliente(persona1)##Bueno me deja agregar sin problemas
banco1.agregar_cliente(persona2)##En el segundo se rompia
banco1.mostrar_clientes()##Funciona bien / Me sigue saltando el none . Realmente no veo donde esta
#Se que es un problema de impresion pero ya toque todo
cuenta = CuentaCorriente(persona1,900,banco1)## instancie el objeto del tipo cuenta
print("Los datos del dueño de la cuenta son:")
cuenta.datos_dueno()
print("Y lo datos del banco son:")
cuenta.datos_banco()



print(f"Datos del dueno: ${cuenta.datos_dueno()}") #Preguntar si esta bien hacer esto
##Porque devuelve lo que quiero pero no es limpio
print(f"Saldo inicial: ${cuenta.get_saldo()}")
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(1500)
print(f"Saldo inicial: ${cuenta.get_saldo()}")