#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

#Programa que muestra todos los números primos dentro de un rango dado

# Límite inferior del rango (desde dónde empezar a buscar)
lower = 1

# Límite superior del rango (hasta dónde buscar)
upper = 500

# Mensaje inicial que indica el rango de búsqueda
print("Prime numbers between", lower, "and", upper, "are:")

# Recorre todos los números desde 'lower' hasta 'upper' inclusive
for num in range(lower, upper + 1):

   # Los números primos son mayores que 1
   if num > 1:

       # Se verifica si el número es divisible por algún valor entre 2 y num-1
       for i in range(2, num):

           # Si el número es divisible, no es primo
           if (num % i) == 0:
               break  # Se corta el bucle porque ya se comprobó que no es primo

       else:
           # Si no se encontró ningún divisor, el número es primo
           print(num)
