# Punto 2.a

pago_original = 14000
tasa_mensual = 0.01
meses_demora = 2

# Pago equivalente en el mes 14
pago_mes_14 = pago_original * (1 + tasa_mensual) ** meses_demora

print("Punto 2.a")
print(f"Pago original en el mes 12: ${pago_original:.2f}")
print(f"Pago equivalente en el mes 14: ${pago_mes_14:.2f}")



# Punto 2.b

costo_mensual = 1000
meses_original = 12
meses_nuevo = 6
pago_original = 14000
tasa_mensual = 0.01

# Valor presente de los costos del proyecto original (12 meses)
vp_costos_original = 0

for mes in range(1, meses_original + 1):
    vp_costos_original += costo_mensual / (1 + tasa_mensual) ** mes

# Valor presente del pago original recibido en el mes 12
vp_pago_original = pago_original / (1 + tasa_mensual) ** meses_original

# VPN original del proveedor
vpn_original = vp_pago_original - vp_costos_original


# Valor presente de los costos del nuevo proyecto (6 meses)
vp_costos_nuevo = 0

for mes in range(1, meses_nuevo + 1):
    vp_costos_nuevo += costo_mensual / (1 + tasa_mensual) ** mes

# Para mantener el mismo VPN:
# VP del nuevo pago = VPN original + VP de los nuevos costos
vp_pago_nuevo = vpn_original + vp_costos_nuevo

# El pago se realizará igualmente en el mes 12
pago_nuevo = vp_pago_nuevo * (1 + tasa_mensual) ** meses_original

print("\nPunto 2.b")
print(f"VPN original del proveedor: ${vpn_original:.2f}")
print(f"Valor presente de los costos a 6 meses: ${vp_costos_nuevo:.2f}")
print(f"Pago necesario en el mes 12: ${pago_nuevo:.2f}")



# Punto 2.c

# Para mantener el mismo VPN:
# VP del pago = VPN original + VP de los costos a 6 meses
vp_pago_mes6 = vpn_original + vp_costos_nuevo

# El pago se realiza al finalizar el proyecto, en el mes 6
pago_mes6 = vp_pago_mes6 * (1 + tasa_mensual) ** meses_nuevo

print("\nPunto 2.c")
print(f"VPN original del proveedor: ${vpn_original:.2f}")
print(f"Valor presente de los costos a 6 meses: ${vp_costos_nuevo:.2f}")
print(f"Pago necesario en el mes 6: ${pago_mes6:.2f}")




# Punto 14.a
# Definición de las tareas del proyecto

tareas = {
    "A": {"duracion": 5,  "predecesoras": []},
    "B": {"duracion": 3,  "predecesoras": ["A"]},
    "C": {"duracion": 10, "predecesoras": ["A"]},
    "D": {"duracion": 20, "predecesoras": ["A"]},
    "E": {"duracion": 5,  "predecesoras": ["B", "C"]},
    "F": {"duracion": 6,  "predecesoras": ["B", "C"]},
    "G": {"duracion": 7,  "predecesoras": ["B", "C"]},
    "H": {"duracion": 10, "predecesoras": ["E", "F", "D"]},
    "I": {"duracion": 9,  "predecesoras": ["G", "D"]},
    "J": {"duracion": 12, "predecesoras": ["H", "I"]}
}

print(tareas)


# Cálculo de inicio y fin temprano de cada tarea

for tarea, datos in tareas.items():

    # Si la tarea no tiene predecesoras, comienza en el día 0
    if not datos["predecesoras"]:
        inicio = 0

    # Si tiene predecesoras, debe esperar a que terminen todas
    else:
        inicio = max(
            tareas[p]["fin"]
            for p in datos["predecesoras"]
        )

    # El fin se obtiene sumando la duración al inicio
    fin = inicio + datos["duracion"]

    # Guardamos los resultados
    datos["inicio"] = inicio
    datos["fin"] = fin


# Mostrar los resultados
print("\nPunto 14.a - Calendarización con recursos infinitos")

for tarea, datos in tareas.items():
    print(
        f"Tarea {tarea}: "
        f"Inicio = {datos['inicio']}, "
        f"Fin = {datos['fin']}"
    )



# Duración total del proyecto
duracion_proyecto = max(datos["fin"] for datos in tareas.values())

# Calcular sucesoras de cada tarea
for tarea in tareas:
    tareas[tarea]["sucesoras"] = []

for tarea, datos in tareas.items():
    for predecesora in datos["predecesoras"]:
        tareas[predecesora]["sucesoras"].append(tarea)


# Cálculo hacia atrás: inicio y fin tardío
for tarea in reversed(list(tareas.keys())):
    datos = tareas[tarea]

    # Si no tiene sucesoras, debe terminar al finalizar el proyecto
    if not datos["sucesoras"]:
        fin_tardio = duracion_proyecto

    # Si tiene sucesoras, tomamos el menor inicio tardío
    else:
        fin_tardio = min(
            tareas[s]["inicio_tardio"]
            for s in datos["sucesoras"]
        )

    inicio_tardio = fin_tardio - datos["duracion"]

    datos["fin_tardio"] = fin_tardio
    datos["inicio_tardio"] = inicio_tardio

    # Holgura
    datos["holgura"] = inicio_tardio - datos["inicio"]


# Mostrar resultados
print("\nDuración total del proyecto:", duracion_proyecto, "días")

print("\nTareas y holguras:")
for tarea, datos in tareas.items():
    print(
        f"Tarea {tarea}: "
        f"Inicio temprano = {datos['inicio']}, "
        f"Inicio tardío = {datos['inicio_tardio']}, "
        f"Holgura = {datos['holgura']}"
    )


# Identificar camino crítico
camino_critico = [
    tarea
    for tarea, datos in tareas.items()
    if datos["holgura"] == 0
]

print("\nCamino crítico:", " -> ".join(camino_critico))


