# Programa que verifica si una reina en un tablero imaginario de ajedrez de 8*8 puede atacar otra ficha en el tablero

a = False
while not a:  # Esta vez escribi el codigo en ingles para variar
    print("Remember to enter columns and rows between 1 and 8")
    print("\n Enter the position of the queen")
    column = int(input("Enter the column: "))

    if column < 1 or column > 8:
        continue

    row = int(input("Enter the row: "))

    if row < 1 or row > 8:
        continue

    print("Enter the position of the target")
    columnTarget = int(input("Enter the column: "))
    if columnTarget < 1 or columnTarget > 8:
        continue

    rowTarget = int(input("Enter the row: "))

    if rowTarget < 1 or rowTarget > 8:
        continue

    if row == rowTarget:
        print("Yes")
        break

    if column == columnTarget:
        print("Yes")
        break

    for i in range(1, 9):
        if columnTarget == column + i and rowTarget == row + i:
            print("Yes")
            a = True
            break
        if columnTarget == column - i and rowTarget == row - i:
            print("Yes")
            a = True
            break
        if columnTarget == column + i and rowTarget == row - i:
            print("Yes")
            a = True
            break
        if columnTarget == column - i and rowTarget == row + i:
            print("Yes")
            a = True
            break

    else:
        print("No")
        break