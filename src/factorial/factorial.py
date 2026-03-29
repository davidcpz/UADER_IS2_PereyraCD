#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
#import sys
#def factorial(num): 
#    if num < 0: 
#        print("Factorial de un número negativo no existe")
#        return 0
#    elif num == 0: 
#        return 1
        
#    else: 
#        fact = 1
#        while(num > 1): 
#            fact *= num 
#            num -= 1
#        return fact 

# Verifico si se ingresó un argumento por línea de comandos
# sys.argv siempre tiene al menos 1 elemento (el nombre del script)
# por eso, si es menor a 2 significa que NO se ingresó ningún número
#if len(sys.argv) < 2:
    # Si no se pasó un número como argumento, se solicita al usuario
    #num = int(input("Ingrese un número: "))
#else:
    # Si se pasó un argumento, se toma ese valor
    #num = int(sys.argv[1])

# Se muestra el resultado del factorial
#print("Factorial ", num, "! es ", factorial(num))


# Obtengo el valor (puede ser número o rango)
#if len(sys.argv) < 2:
#    valor = input("Ingrese un número o rango: ")
#else:
#    valor = sys.argv[1]

# Verifico si es un rango
#if "-" in valor:
    # Separo los valores del rango
#    partes = valor.split("-")
    
#    desde = int(partes[0])
#    hasta = int(partes[1])

    # Recorro el rango y calculo factorial de cada número
#    for i in range(desde, hasta + 1):
#        print("Factorial ", i, "! es ", factorial(i))

#else:
    # Si es un número, lo convierto a entero
#    num = int(valor)
    
    # Muestro el resultado
#    print("Factorial ", num, "! es ", factorial(num))


#CODIGO REFACTORIZADO PARA QUE PUEDA RECIBIR NUMEROS 
#SIN LIMITE INFERIOR Y SIN LIMITE SUPERIOR
import sys

# Función que calcula el factorial de un número
def factorial(num): 
    # Si el número es negativo, el factorial no existe
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    
    # El factorial de 0 es 1
    elif num == 0: 
        return 1
    
    # Cálculo iterativo del factorial para números mayores a 0
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verifico si se ingresó un argumento por línea de comandos
# Si no se ingresó, lo solicito por teclado
if len(sys.argv) < 2:
    valor = input("Ingrese un número o rango: ")
else:
    valor = sys.argv[1]

# Verifico si el valor ingresado contiene un guion
# Si contiene "-", puede ser un rango
if "-" in valor:
    # Separo las dos partes del rango
    partes = valor.split("-")

    # Caso 1: rango sin límite inferior, por ejemplo "-10"
    if partes[0] == "":
        desde = 1
        hasta = int(partes[1])

    # Caso 2: rango sin límite superior, por ejemplo "5-"
    elif partes[1] == "":
        desde = int(partes[0])
        hasta = 60

    # Caso 3: rango completo, por ejemplo "4-8"
    else:
        desde = int(partes[0])
        hasta = int(partes[1])

    # Recorro el rango y muestro el factorial de cada número
    for i in range(desde, hasta + 1):
        print("Factorial ", i, "! es ", factorial(i))

# Si no hay guion, se interpreta como un número único
else:
    num = int(valor)
    print("Factorial ", num, "! es ", factorial(num))