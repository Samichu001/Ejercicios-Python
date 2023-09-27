def mayorYmenor(tabla):
    if not tabla:
        print("La tabla esta vacia.")
        return
    mayor = menor = tabla[0]
    for palabra in tabla:
        if len(palabra) > len(mayor):
            mayor = palabra
        elif len(palabra) < len(menor):
            menor = palabra
    print("La palabra con mayor longitud es: ", mayor)
    print("La palabra con menor longitud es: ", menor)

tabla = ["hola", "adios", "carlos", "mercurio", "aguacate", "geminis"]
mayorYmenor(tabla)