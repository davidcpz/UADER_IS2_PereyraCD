import numpy as np
import matplotlib.pyplot as plt


def calcular_esfuerzo(s):
    return 8 * (s ** 0.95)


def calcular_tiempo(esfuerzo):
    return 2.4 * (esfuerzo ** 0.33)


# -----------------------------------
# Valores para E en función de S
# -----------------------------------

tamanios = np.arange(0, 10001, 10)
esfuerzos = calcular_esfuerzo(tamanios)

print("\nPrimeros valores E vs S:")
print("Tamaño S\tEsfuerzo E")

for i in range(10):
    print(f"{tamanios[i]:.1f}\t\t{esfuerzos[i]:.6f}")


# Gráfico 1
plt.figure()
plt.plot(tamanios, esfuerzos)
plt.title("Esfuerzo en función del tamaño del proyecto")
plt.xlabel("Tamaño S")
plt.ylabel("Esfuerzo E")
plt.grid()
plt.savefig("esfuerzo_vs_tamanio.png")
plt.show()


# -----------------------------------
# Valores para td en función de E
# -----------------------------------

esfuerzos_td = np.arange(1, 501, 1)
tiempos = calcular_tiempo(esfuerzos_td)

print("\nPrimeros valores td vs E:")
print("Esfuerzo E\tTiempo td")

for i in range(10):
    print(f"{esfuerzos_td[i]:.1f}\t\t{tiempos[i]:.6f}")


# Gráfico 2
plt.figure()
plt.plot(esfuerzos_td, tiempos)
plt.title("Tiempo calendario en función del esfuerzo")
plt.xlabel("Esfuerzo E")
plt.ylabel("Tiempo calendario td")
plt.grid()
plt.savefig("tiempo_vs_esfuerzo.png")
plt.show()