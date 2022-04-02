# Programa que organiza una lista, poniendo los ceros a la derecha y los demas numeros en orden a la izquierda

List = [4, 0, 5, 0, 3, 0, 0, 5]  # Ejemplo de lista
count = 0

for i in List:
    if i != 0:
        print(i,",", end="")
    else:
        count += 1
for i in range(count):
    if i == count-1:
        print(0, end="")
    else:
        print(0,",", end="")
