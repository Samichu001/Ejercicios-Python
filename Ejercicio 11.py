salarios = [[700, 900, 1300], [1000, 950, 1080], [1300, 930, 1200]]

empleados = ["Javier Maria", "Anotnio Muñoz", "Isabel Allende"]

for x in range(len(empleados)):
    nombre_empleado = empleados[x]
    salario_separado = salarios[x]
    salario_total = sum(salario_separado)

    print(nombre_empleado, " + ", salario_separado, " = ", salario_total)