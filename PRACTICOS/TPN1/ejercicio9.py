print("Desarrolle un programa que indique cómo es un número ingresado por el usuario con respecto a otro que es generado aleatoriamente del 1 al 10 al comenzar el programa.Debe de evaluar si es igual, menor, mayor, distinto, menor o igual y mayor o igual.")
import random
numero = int(input("Ingrese un numero"))
rand = random.randint(1,10)
print("El numero ingresado por tablero es" , numero , "el numero generado aleatoriamente fue:" ,rand)
if (numero == rand):
    print("Los numeros son iguales")
else:
    print("Los numeros son distintos")
    if (numero > rand):
        print(numero,"es mayor a", rand)
    elif (numero < rand ):
        print(numero,"es menor que", rand)
        if (numero >= rand):
            print(numero,"es mayor que", rand)
        elif(numero <= rand):
            print(numero,"es menor e igual que:",rand)
