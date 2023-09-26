cadena = str(input("Introduce una cadena de caracteres"))

contador = 0

for i in range(len(cadena) - 2):
    if cadena[i:i+3] == "aaa":
        contador += 1

print("La subadena aaa ha aparecido", contador, "veces")