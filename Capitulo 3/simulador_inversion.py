#Datos
print("Bienvenido al simulador de inversiones!")
print("-" * 50)

monto_inicial = float(input("Ingresa el monto inicial: $"))
tasa_interes = float(input("Ingresa la tasa de interés anual (%): "))
anios = int(input("¿Cuántos años planeas invertir?: "))
saldo_acumulado = monto_inicial

print("\n---Simulacion de inversión---")

#Bucle for
for anio in range(1, anios + 1):
    ganacia = saldo_acumulado * (tasa_interes / 100)
    saldo_acumulado += ganacia
    print(f"Año {anio}: ${saldo_acumulado:.2f} (Ganancia: ${ganacia:.2f})")



#Reporte
print("Reporte final de inversión:")
print("=" * 50)
print(f"Monto inicial: ${monto_inicial:.2f}")
print(f"Tasa de interés: {tasa_interes}%")
print(f"Años invertidos: {anios}")
print(f"Ganancia total: ${saldo_acumulado - monto_inicial:.2f}")
print(f"Total acumulado: ${saldo_acumulado:.2f}")
print("=" * 50)