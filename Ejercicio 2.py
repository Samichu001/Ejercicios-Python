cantidad_ceros = 0
cantidad_mayor_cero = 0
cantidad_menor_cero = 0

for i in range(10):
    numero = int(input("Introduce 10 numeros enteros"))

    if numero == 0:
        cantidad_ceros += 1
    elif numero > 0:
        cantidad_mayor_cero += 1
    else:
        cantidad_menor_cero += 1

print("Has introducido un total de ", cantidad_ceros, "ceros")
print("Has introducido un total de ", cantidad_mayor_cero, "numeros mas grandes que 0")
print("Has introducido un total de ", cantidad_menor_cero, "numeros mas pequeños que 0")