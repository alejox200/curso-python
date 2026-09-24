#Datos
print("Bienvenido al Sistema de Peaje Inteligente de Autopista")
tipo_vehiculo = input("Ingrese el tipo de vehiculo: (moto/coche/bus)").strip().lower()
hour = float(input("Ingrese la hora del peaje (Formato militar 24hrs): "))
dispositivo = input("¿Poseé dispositivo electrónico de Telepeaje? (si/no)").strip().lower()

#Funcionamiento matematico de condicionales anidados
if hour >= 7 and hour <= 9 or hour >= 17 and hour <= 19:
    if tipo_vehiculo == "moto":
        tarifa = 15.0
    elif tipo_vehiculo == "coche":
        tarifa = 30.0
    elif tipo_vehiculo == "bus":
        tarifa = 60.0
    else:
        print("Vehiculo no reconocido")

    if dispositivo == "si":
        tarifa -= (tarifa * 0.10)
    
    print(f"La tarifa en hora pico es de ${tarifa}")
else:
    if tipo_vehiculo == "moto":
        tarifa = 10.0
    elif tipo_vehiculo == "coche":
        tarifa = 20.0
    elif tipo_vehiculo == "bus":
        tarifa = 40.0
    else:
        print("Vehiculo no reconocido")
    
    if dispositivo == "si":
        tarifa -= (tarifa * 0.05)
    
    print(f"La tarifa es de ${tarifa}")

#Operador ternario
if dispositivo == "si":
    descuento = "Aplicado"
else:
    descuento = "No aplicado"

if descuento == "Aplicado":
    print(f"Su descuento es: {descuento} y tiene un 10% de descuento")
else:
    print(f"No tiene descuento por el momento: {descuento}")

print(f"Gracias por utilizar el sistema")
print("=" * 40)
print(f"Hora del peaje: {hour}")
print(f"Tipo de vehiculo: {tipo_vehiculo}")
print(f"Dispositivo: {dispositivo}")
print(f"Tarifda: ${tarifa}")
print("=" * 40)
    
