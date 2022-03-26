# Programa que simula un cajero automatico
# Al sacar dinero dara billetes de 50.000, 20.000 y 10.000

import time
from os import system


class Billetes:
    def __init__(self, valor, cantidad):
        self.valor = valor
        self.cantidad = cantidad


def historial(lista, cantidad):
    lista.append(cantidad)


def imprimir_historial(lista):
    print("Historial de retiros: ")
    j = 1
    for i in lista:
        print("#", j, " retiro por valor de: ", i)
        j += 1


def dinero_total():
    dinero = 0
    dinero += Billete_50.cantidad * Billete_50.valor
    dinero += Billete_20.cantidad * Billete_20.valor
    dinero += Billete_10.cantidad * Billete_10.valor
    return dinero


# El dinero inicial con el que cuenta el cajero automatico es 5.000.000
Billete_50 = Billetes(50000, 50)  # La mitad del dinero inicial esta en billetes de 50.000
Billete_20 = Billetes(20000, 100)  # La otra mitad del dinero inicial esta en billetes de 20.000 y 10.000
Billete_10 = Billetes(10000, 50)
Opcion = 0
Historial_retiros = []

while Opcion != 4:
    system("cls")
    print("\n \n")
    print("__Menu Cajero Automatico__")
    print("1. Retirar dinero")  # Puede retirar como maximo 600.000
    print("2. Consultar dinero y billetes del cajero automatico")
    print("3. Historial de retiros")
    print("4. Salir \n")
    Opcion = int(input("Ingrese la opcion que quiere elegir:\n"))

    if Opcion == 1:
        Retiro = int(input("Ingrese la cantidad de dinero que desea retirar (Maximo 600.000)\n"))
        Retiro_aux = Retiro

        if Retiro > 600000:
            print("El monto a retirar excede el maximo de 600.000")
            time.sleep(5)
            continue

        if Retiro < 10000:
            print("El monto a retirar es demasiado pequeño, el monto debe ser minimo 10.000")
            time.sleep(5)
            continue

        if Retiro % 10000 != 0:
            print("El monto a retirar no es multiplo de 10.000, ejemplos: 50.000, 100.000, 130.000")
            time.sleep(5)
            continue

        if Retiro > dinero_total():
            print("El monto a retirar excede el dinero disponible en este momento")
            print("El monto maximo que puede retirar en este momento es ", dinero_total())
            time.sleep(5)
            continue

        if Retiro < 50000:
            if Retiro == 40000 and Billete_20.cantidad >= 1 and Billete_10.cantidad >= 2:
                print("El cajero entrega 1 billete de 20.000 y 2 billetes de 10.000")
                Billete_20.cantidad -= 1
                Billete_10.cantidad -= 2
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue

            if Retiro == 40000 and Billete_20.cantidad >= 2:
                print("El cajero entrega 2 billetes de 20.000")
                Billete_20.cantidad -= 2
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue

            if Retiro == 30000 and Billete_10.cantidad >= 1 and Billete_20.cantidad >= 1:
                print("El cajero entrega 1 billete de 20.000 y 1 billete de 10.000")
                Billete_20.cantidad -= 1
                Billete_10.cantidad -= 1
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue

            if Retiro == 30000 and Billete_10.cantidad >= 3:
                print("El cajero entrega 3 billetes de 10.000")
                Billete_10.cantidad -= 3
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue

            if Retiro == 20000 and Billete_10.cantidad >= 2:
                print("El cajero entrega 2 billetes de 10.000")
                Billete_10.cantidad -= 2
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue

            if Retiro == 20000 and Billete_20.cantidad >= 1:
                print("El cajero entrega 1 billete de 20.000")
                Billete_20.cantidad -= 1
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue

            if Retiro == 10000 and Billete_10.cantidad > 0:
                print("El cajero entrega 1 billete de 10.000")
                Billete_10.cantidad -= 1
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue

            print("No tenemos suficientes billetes para su retiro")
            time.sleep(5)
            continue

        if Retiro == 50000:
            if Billete_10.cantidad >= 1 and Billete_20.cantidad >= 2:
                print("El cajero entrega 2 billetes de 20.000 y 1 billete de 10.000")
                Billete_10.cantidad -= 1
                Billete_20.cantidad -= 2
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue
            elif Billete_50.cantidad >= 1:
                print("El cajero entrega 1 billete de 50.000")
                Billete_50.cantidad -= 1
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue
            elif Billete_10.cantidad >= 5:
                print("El cajero entrega 5 billetes de 10.000")
                Billete_10.cantidad -= 5
                historial(Historial_retiros, Retiro)
                time.sleep(5)
                continue
            else:
                print("No tenemos suficientes billetes para su retiro")
                time.sleep(5)
                continue

        if Retiro > 50000:
            if Billete_10.cantidad > 0 and Billete_20.cantidad >= 2 and Billete_50.cantidad > 0:
                Retiro -= 50000

                if Billete_50.cantidad > 0:
                    Billete_50_retiro = Retiro // Billete_50.valor

                    if Billete_50.cantidad >= Billete_50_retiro:
                        Retiro -= Billete_50_retiro * Billete_50.valor
                    else:
                        Billete_50_retiro = Billete_50.cantidad
                        Retiro -= Billete_50_retiro * Billete_50.valor

                if Billete_20.cantidad > 0:
                    Billete_20_retiro = Retiro // Billete_20.valor

                    if Billete_20.cantidad >= Billete_20_retiro:
                        Retiro -= Billete_20_retiro * Billete_20.valor
                    else:
                        Billete_20_retiro = Billete_20.cantidad
                        Retiro -= Billete_20_retiro * Billete_20.valor

                if Billete_10.cantidad > 0:
                    Billete_10_retiro = Retiro // Billete_10.valor

                    if Billete_10.cantidad >= Billete_10_retiro:
                        Retiro -= Billete_10_retiro * Billete_10.valor
                    else:
                        Billete_10_retiro = Billete_10.cantidad
                        Retiro -= Billete_10_retiro * Billete_10.valor

                if Retiro == 0:
                    print("El cajero entrega ", Billete_50_retiro, " billetes de 50.000")
                    print("El cajero entrega ", Billete_20_retiro+2, " billetes de 20.000")
                    print("El cajero entrega ", Billete_10_retiro+1, " billetes de 10.000")
                    Billete_50.cantidad -= Billete_50_retiro
                    Billete_20.cantidad -= Billete_20_retiro
                    Billete_10.cantidad -= Billete_10_retiro
                    historial(Historial_retiros, Retiro_aux)
                    time.sleep(5)
                    continue
                else:
                    print("No hay billetes para entregar el retiro solicitado")
                    time.sleep(5)
                    continue

            elif Billete_10.cantidad > 0 and Billete_20.cantidad > 0 and Billete_50.cantidad > 0:
                if Billete_50.cantidad > 0:
                    Billete_50_retiro = Retiro // Billete_50.valor

                    if Billete_50.cantidad >= Billete_50_retiro:
                        Retiro -= Billete_50_retiro * Billete_50.valor
                    else:
                        Billete_50_retiro = Billete_50.cantidad
                        Retiro -= Billete_50_retiro * Billete_50.valor

                if Billete_20.cantidad > 0:
                    Billete_20_retiro = Retiro // Billete_20.valor

                    if Billete_20.cantidad >= Billete_20_retiro:
                        Retiro -= Billete_20_retiro * Billete_20.valor
                    else:
                        Billete_20_retiro = Billete_20.cantidad
                        Retiro -= Billete_20_retiro * Billete_20.valor

                if Billete_10.cantidad > 0:
                    Billete_10_retiro = Retiro // Billete_10.valor

                    if Billete_10.cantidad >= Billete_10_retiro:
                        Retiro -= Billete_10_retiro * Billete_10.valor
                    else:
                        Billete_10_retiro = Billete_10.cantidad
                        Retiro -= Billete_10_retiro * Billete_10.valor

                if Retiro == 0:
                    print("El cajero entrega ", Billete_50_retiro, " billetes de 50.000")
                    print("El cajero entrega ", Billete_20_retiro, " billetes de 20.000")
                    print("El cajero entrega ", Billete_10_retiro, " billetes de 10.000")
                    Billete_50.cantidad -= Billete_50_retiro
                    Billete_20.cantidad -= Billete_20_retiro
                    Billete_10.cantidad -= Billete_10_retiro
                    historial(Historial_retiros, Retiro_aux)
                    time.sleep(5)
                    continue
                else:
                    print("No hay billetes para entregar el retiro solicitado")
                    time.sleep(5)
                    continue

    if Opcion == 2:
        print("La cantidad de dinero que tiene el cajero automatico es: ", dinero_total())
        print("El cajeto tiene ", Billete_50.cantidad, " billetes de 50.000")
        print("El cajeto tiene ", Billete_20.cantidad, " billetes de 20.000")
        print("El cajeto tiene ", Billete_10.cantidad, " billetes de 10.000")
        time.sleep(7)
        continue

    if Opcion == 3:
        imprimir_historial(Historial_retiros)
        time.sleep(10)
        continue

    if Opcion == 4:
        break

    else:
        print("Porfavor eliga una opcion correcta")
        time.sleep(5)
        continue

print("Hasta luego")
time.sleep(5)
exit()
