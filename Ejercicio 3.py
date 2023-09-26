import random

aleatorio = random.randint(0, 20)
numero = 0

while numero != aleatorio:
    numero = int(input("Intenta adivinar que numero del 0 al 20 ha salido"))
    if numero < aleatorio:
        print("El numero es mayor")
    elif numero > aleatorio:
        print("El numero es mas pequeño")
    else:
        print("Enhorabuena!!!")
        break