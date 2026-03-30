# Función que calcula la cantidad de iteraciones de Collatz para un número
def collatz(n):
    pasos = 0

    while n != 1:
        # Si el número es par
        if n % 2 == 0:
            n = n // 2  # División entera
        else:
            # Si es impar
            n = 3 * n + 1

        pasos += 1

    return pasos


# Listas para almacenar resultados
numeros = []
iteraciones = []

# Recorro números del 1 al 100 (después lo cambiamos a 10000)
for i in range(1, 10001):
    pasos = collatz(i)

    numeros.append(i)
    iteraciones.append(pasos)

    print(i, "→", pasos)

    import matplotlib.pyplot as plt

# Crear gráfico
plt.plot(iteraciones, numeros)

# Etiquetas
plt.xlabel("Cantidad de iteraciones")
plt.ylabel("Número inicial")

# Título
plt.title("Conjetura de Collatz")

# Mostrar gráfico
plt.show()