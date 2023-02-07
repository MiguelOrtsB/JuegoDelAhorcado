# Ahorcado

import random

# Lista de palabras para el juego del ahorcado
lista_palabras = ["gato", "pueblo", "roca", "mesa", "sol", "palo", "tiburon", "avion", "uva", "pera", "pez", "nube", "cielo", "mosca", "regaliz"]

# Seleccionar una palabra al azar de la lista de palabras
palabra_elegida = random.choice(lista_palabras)

# Crear una lista vacía para guardar las letras adivinadas
letras_adivinadas = []

# Variable que controla el número de intentos
intentos = 0

# Variable que controla si el juego ha terminado o no
juego_terminado = False

# Mientras el juego no haya terminado, seguir jugando
while not juego_terminado:

    # Mostrar la palabra con los espacios en blanco por las letras no adivinadas aún
    for letra in palabra_elegida:

        if letra in letras_adivinadas:

            print(letra, end=" ")

        else:

            print(" _ ", end=" ")

    print()

    # Pedir al usuario que ingrese una letra para adivinar
    letra_ingresada = input("Ingresa una letra: ")

    # Si la letra ingresada está en la palabra elegida, agregarla a la lista de letras adivinadas y mostrar un mensaje al usuario. De lo contrario, sumar 1 al número de intentos.
    if letra_ingresada in palabra_elegida:

        print("¡Correcto!")
        letras_adivinadas.append(letra_ingresada)

        if len(letras_adivinadas) == len(palabra_elegida):
            juego_terminado = True
            print("Juego terminado. Ganaste")

    # Si se llega al número de intentos establecido, se termina el juego
    else:

        print("Incorrecto")
        intentos += 1

        if intentos == 1:
            print(" +---+")
            print(" |   |")
            print(" 0   |")
            print("     |")
            print("     |")
            print("     |")
            print(" ======")

        if intentos == 2:
            print(" +---+")
            print(" |   |")
            print(" 0   |")
            print(" |   |")
            print("     |")
            print("     |")
            print(" ======")

        if intentos == 3:
            print(" +---+")
            print(" |   |")
            print(" 0   |")
            print("/|   |")
            print("     |")
            print("     |")
            print(" ======")

        if intentos == 4:
            print(" +---+")
            print(" |   |")
            print(" 0   |")
            print("/|\  |")
            print("     |")
            print("     |")
            print(" ======")

        if intentos == 5:
            print(" +---+")
            print(" |   |")
            print(" 0   |")
            print("/|\  |")
            print("/    |")
            print("     |")
            print(" ======")

        if intentos == 6:
            juego_terminado = True
            print(" +---+")
            print(" |   |")
            print(" 0   |")
            print("/|\  |")
            print("/ \  |")
            print("     |")
            print(" ======")
            print("Juego terminado. Ahorcado")
