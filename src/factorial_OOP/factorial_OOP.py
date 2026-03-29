import sys

class Factorial:
    # Constructor de la clase
    def __init__(self):
        pass

    # Método que calcula el factorial de un número
    def factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    # Método que recorre un rango y calcula el factorial de cada número
    def run(self, min, max):
        for i in range(min, max + 1):
            print("Factorial ", i, "! es ", self.factorial(i))


# Programa principal
obj = Factorial()

# Si se ingresa un argumento, se usa ese valor
if len(sys.argv) >= 2:
    valor = sys.argv[1]

    # Si hay un guion, se interpreta como rango
    if "-" in valor:
        partes = valor.split("-")

        if partes[0] == "":
            desde = 1
            hasta = int(partes[1])
        elif partes[1] == "":
            desde = int(partes[0])
            hasta = 60
        else:
            desde = int(partes[0])
            hasta = int(partes[1])

        obj.run(desde, hasta)

    # Si no hay guion, se calcula solo un número
    else:
        num = int(valor)
        obj.run(num, num)

# Si no se ingresa argumento, se solicita por teclado
else:
    valor = input("Ingrese un número o rango: ")

    if "-" in valor:
        partes = valor.split("-")

        if partes[0] == "":
            desde = 1
            hasta = int(partes[1])
        elif partes[1] == "":
            desde = int(partes[0])
            hasta = 60
        else:
            desde = int(partes[0])
            hasta = int(partes[1])

        obj.run(desde, hasta)
    else:
        num = int(valor)
        obj.run(num, num)