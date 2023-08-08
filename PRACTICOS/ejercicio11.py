import random

partidas_ganadas = 0
partidas_perdidas = 0

def jugar_partida():
    global partidas_ganadas, partidas_perdidas

    while True:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        if num1 != num2:
            break

    print("Valores generados:", num1, num2)

    while True:
        try:
            apuesta = int(input("¿Apuestas por el valor 1 o el valor 2? "))
            if apuesta not in (1, 2):
                print("Debes ingresar 1 o 2.")
            else:
                break
        except ValueError:
            print("Ingresa un valor numérico.")

    if apuesta == 1:
        ganador = max(num1, num2)
        perdedor = min(num1, num2)
    else:
        ganador = min(num1, num2)
        perdedor = max(num1, num2)

    print("El valor ganador es:", ganador)
    if apuesta == ganador:
        print("¡Has ganado!")
        partidas_ganadas += 1
    else:
        print("Has perdido.")
        partidas_perdidas += 1

while True:
    jugar_partida()
    respuesta = input("¿Quieres volver a jugar? (s/n): ")
    if respuesta.lower() != "s":
        break

print("Partidas ganadas:", partidas_ganadas)
print("Partidas perdidas:", partidas_perdidas)