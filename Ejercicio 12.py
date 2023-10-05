class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    
    def get_titular(self):
        return self.titular

    def set_titular(self, nuevo_titular):
        self.titular = nuevo_titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def ingresar(self):
        cantidad = float(input("Introduzca una cantidad de dinero"))
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad introducida debe ser positiva")

    def retirar(self):
        cantidad = float(input("seleccione la cantidad que desea retirar"))
        if cantidad > 0:
            self.cantidad -= cantidad
            if cantidad < 0:
                self.cantidad = 0
        else:
            print("La cantidad introducida debe de ser positiva")
    
    def __str__(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad}"

titular = str(input("Ingrese el nombre del titular de la cuenta: "))
saldo_inicial = float(input("Ingrese la cantidad inicial de la cuenta"))
mi_cuenta = Cuenta(titular, saldo_inicial)
print(mi_cuenta)

mi_cuenta.ingresar()
print(mi_cuenta)