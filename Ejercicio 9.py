tabla = ["manzana", "platano", "cereza", "uva", "pera"]
buscar_cadena = "cereza"

def indexContains(tabla, cadena):
    for i, valor in enumerate(tabla):
        if valor == cadena:
            return i
    return -1

indice = indexContains(tabla, buscar_cadena)

if indice != -1:
    print("El valor ", buscar_cadena, " se encuentra en el índice")
else:
    print("El valor ", buscar_cadena, "No se encuentra en el indice")