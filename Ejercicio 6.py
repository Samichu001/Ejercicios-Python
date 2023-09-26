cadena = str(input("Introduce una cadena de caracteres"))

if len(cadena) >= 2:
    primero = cadena[0]
    ultimo = cadena[-1]

    cadena_intercambiada = ultimo + cadena[1:-1] + primero

    print(cadena_intercambiada)

else:
    print("La cadena de caracteres debe tener al menos dos caracteres")