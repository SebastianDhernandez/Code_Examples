# Programa que edita texto

import time
from os import system


def menu():
    print("____MENU____")
    print("1. Ingresar un texto")
    print("2. Encontrar un subtexto del texto")
    print("3. Añadir algo al texto")
    print("4. Eliminar algo del texto")
    print("5. Salir")


Opcion = 0
Texto = ""

while Opcion != 5:
    system("cls")
    menu()
    Opcion = int(input("Ingrese la opcion que desea elegir\n"))

    if Opcion == 1:
        Texto = str(input("Ingrese el texto\n"))
        continue

    if Opcion == 2:
        Subtexto = str(input("Ingrese el subtexto o caracter que desea hallar\n"))
        Hallar = Texto.find(Subtexto)
        Palabra = Subtexto.find(" ")

        if Hallar == -1:
            print("No se hallo el subtexto o caracter en el texto original")
            time.sleep(5)
            continue

        if Palabra != -1:
            print("El subtexto se encuentra en el texto desde la posicion del string ", Hallar, " hasta ",
                  Hallar+len(Subtexto)-1)
            Numero = Texto.count(Subtexto)
            print("Numero de veces que se encuentra en el texto: ", Numero)
            time.sleep(5)
            continue

        if Palabra == -1:
            print("La palabra o caracter si se encuentra en el texto")
            Numero = Texto.count(Subtexto)
            print("Numero de veces que se encuentra en el texto: ", Numero)

            if len(Subtexto) == 1:
                print("La primera vez que se halla el caracter en el texto es en la posicion del string ", Hallar)
            else:
                print("La primera vez que se halla la palabra en el texto es desde la posicion del string ", Hallar,
                      " hasta ", Hallar + len(Subtexto) - 1)

            time.sleep(5)
            continue

    if Opcion == 3:
        Texto_add = str(input("Ingrese el texto que desea añadir al texto original\n"))
        Texto = Texto + Texto_add
        print("El texto resultante es ", Texto)
        time.sleep(5)
        continue

    if Opcion == 4:
        print("¿Que desea eliminar?")
        print("1. Un subtexto (Palabra, caracter o subtexto)")
        print("2. Un subtexto con una posicion especifica")
        print("3. Volver al menu")

        Opcion_delete = int(input("Ingrese la opcion que desea elegir\n"))

        if Opcion_delete == 1:
            Eliminar = str(input("Ingrese el subtexto que desea buscar y eliminar\n"))
            Texto = Texto.replace(Eliminar, "")
            print("El texto resultante es ", Texto)
            time.sleep(5)
            continue

        if Opcion_delete == 2:
            print("Ingrese desde que posicion y hasta que posicion desea eliminar del string")
            Posicion_start = int(input("Ingrese la pocsicion inicial\n"))
            Posicion_end = int(input("Ingrese la posicion final\n"))

            j = 0
            for i in Texto:
                if Posicion_start <= j <= Posicion_end:
                    Texto = Texto.replace(i, "", 1)
                j += 1

            print("El texto resultante es ", Texto)
            time.sleep(5)
            continue

        else:
            continue

    if Opcion == 5:
        break

    else:
        print("Escoja una opcion valida")
        time.sleep(5)
        continue

print("Hasta luego")
time.sleep(3)
exit()
