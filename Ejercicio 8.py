tabla = [1, 2, 3, 4, 5]
resultado = sum(tabla)

def sum(tabla):
    suma = 0
    for elemento in tabla:
        suma += elemento
    return suma

print("La suma de ", tabla, "da como resultado: ", resultado)