# Programa que encuentra el promedio de n numeros ingresados

print("Ingrese la cantidad de numeros que desea promediar")
Cantidad = int(input())
Sumador = 0
Promedio = 0

for p in range(Cantidad):
    print("Ingrese el dato #", p+1)
    Numero = float(input())
    Sumador += Numero

Promedio = Sumador/Cantidad
print("El promedio de los ", Cantidad, " numeros ingresados es: ", Promedio)
