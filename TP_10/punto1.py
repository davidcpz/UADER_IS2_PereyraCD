
# Punto 1

costo_mensual = 1000
meses = 12
beneficio = 18000
tasa = 0.01


# Valor presente de los costos
vp_costos = 0

for mes in range(1, meses + 1):
    vp_costos = vp_costos + costo_mensual / (1 + tasa) ** mes

print("Valor presente de los costos:", vp_costos)

# Valor presente del beneficio
vp_beneficio = beneficio / (1 + tasa) ** meses

print(f"Valor presente del beneficio: ${vp_beneficio:.2f}")

# Valor Presente Neto
vpn = vp_beneficio - vp_costos

print(f"Valor presente neto (VPN): ${vpn:.2f}")

# Punto 1.b

meses_extendido = 15

# Valor presente de los costos durante 15 meses
vp_costos_extendido = 0

for mes in range(1, meses_extendido + 1):
    vp_costos_extendido = vp_costos_extendido + costo_mensual / (1 + tasa) ** mes

print(f"Valor presente de los costos (15 meses): ${vp_costos_extendido:.2f}")



# Valor presente del beneficio recibido en el mes 15
vp_beneficio_extendido = beneficio / (1 + tasa) ** meses_extendido

print(f"Valor presente del beneficio (mes 15): ${vp_beneficio_extendido:.2f}")


# Valor Presente Neto del proyecto extendido
vpn_extendido = vp_beneficio_extendido - vp_costos_extendido

print(f"Valor presente neto (VPN) a 15 meses: ${vpn_extendido:.2f}")


# Punto 1.c

# Rentabilidad del proyecto según lo planificado (12 meses)
rentabilidad_12 = vpn / vp_costos

print(f"Rentabilidad a 12 meses: {rentabilidad_12 * 100:.2f}%")

# Rentabilidad del proyecto extendido (15 meses)
rentabilidad_15 = vpn_extendido / vp_costos_extendido

print(f"Rentabilidad a 15 meses: {rentabilidad_15 * 100:.2f}%")



# Punto 1.d

meses_retraso = 18

# Valor presente de los costos durante 18 meses
vp_costos_retraso = 0

for mes in range(1, meses_retraso + 1):
    vp_costos_retraso = vp_costos_retraso + costo_mensual / (1 + tasa) ** mes

# Valor presente del beneficio recibido en el mes 18
vp_beneficio_retraso = beneficio / (1 + tasa) ** meses_retraso

# Valor Presente Neto con 6 meses de retraso
vpn_retraso = vp_beneficio_retraso - vp_costos_retraso

# Rentabilidad con 6 meses de retraso
rentabilidad_retraso = vpn_retraso / vp_costos_retraso

# Mostrar resultados
print("\nPunto 1.d - Retraso de 6 meses")
print(f"Valor presente de los costos (18 meses): ${vp_costos_retraso:.2f}")
print(f"Valor presente del beneficio (mes 18): ${vp_beneficio_retraso:.2f}")
print(f"Valor presente neto (VPN) a 18 meses: ${vpn_retraso:.2f}")
print(f"Rentabilidad a 18 meses: {rentabilidad_retraso * 100:.2f}%")


# Punto 1.e

porcentaje_gerencia = 0.05

# Costo mensual incluyendo la gerencia profesional
costo_mensual_gerencia = costo_mensual * (1 + porcentaje_gerencia)

# Valor presente de los costos con gerencia durante 12 meses
vp_costos_gerencia = 0

for mes in range(1, meses + 1):
    vp_costos_gerencia = vp_costos_gerencia + costo_mensual_gerencia / (1 + tasa) ** mes

# El beneficio se recibe en el mes 12
vp_beneficio_gerencia = beneficio / (1 + tasa) ** meses

# Valor Presente Neto con gerencia profesional
vpn_gerencia = vp_beneficio_gerencia - vp_costos_gerencia

# Rentabilidad
rentabilidad_gerencia = vpn_gerencia / vp_costos_gerencia

# Mostrar resultados
print("\nPunto 1.e - Gestión profesional")
print(f"Costo mensual con gerencia: ${costo_mensual_gerencia:.2f}")
print(f"Valor presente de los costos: ${vp_costos_gerencia:.2f}")
print(f"Valor presente del beneficio: ${vp_beneficio_gerencia:.2f}")
print(f"Valor presente neto (VPN): ${vpn_gerencia:.2f}")
print(f"Rentabilidad: {rentabilidad_gerencia * 100:.2f}%")


# Punto 1.f

# Queremos mantener el mismo VPN del proyecto original
vpn_objetivo = vpn

# Valor presente máximo permitido para los costos
vp_costos_maximo = vp_beneficio_extendido - vpn_objetivo

# Calculamos el factor de descuento de los 15 meses
factor_costos_15 = 0

for mes in range(1, meses_extendido + 1):
    factor_costos_15 = factor_costos_15 + 1 / (1 + tasa) ** mes

# Costo mensual máximo permitido
costo_mensual_maximo = vp_costos_maximo / factor_costos_15

print("\nPunto 1.f - Costo mensual máximo")
print(f"VPN objetivo: ${vpn_objetivo:.2f}")
print(f"Valor presente del beneficio a 15 meses: ${vp_beneficio_extendido:.2f}")
print(f"Valor presente máximo de los costos: ${vp_costos_maximo:.2f}")
print(f"Costo mensual máximo permitido: ${costo_mensual_maximo:.2f}")






















