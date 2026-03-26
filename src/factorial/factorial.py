#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verifico si se ingresó un argumento por línea de comandos
# sys.argv siempre tiene al menos 1 elemento (el nombre del script)
# por eso, si es menor a 2 significa que NO se ingresó ningún número
if len(sys.argv) < 2:
    # Si no se pasó un número como argumento, se solicita al usuario
    num = int(input("Ingrese un número: "))
else:
    # Si se pasó un argumento, se toma ese valor
    num = int(sys.argv[1])

# Se muestra el resultado del factorial
print("Factorial ", num, "! es ", factorial(num))