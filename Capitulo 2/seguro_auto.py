#Datos
name = input("Ingrese su nombre: ").strip().capitalize()
antiguedad = input("Su vehiculo tiene menos de 10 años de antiguedad? (si/no): ").strip().lower()

#Condicionales
if antiguedad == "si": 
    accidente = int(input("¿Cuantos accidentes has tenido el ultimo año?:"))

    if accidente == 0: 
        economia = 500
    elif accidente <= 2:
        economia = 800
    else:
        accidente >= 3
        economia = 1000
    print(f"Bienvenido {name}, tienes una tarifa de: ${economia}")
else:
    print("=" * 50)
    print(f"Lo sentimos {name}, tu vehiculo es demasiado antiguo para la poliza estandar y debe pasara inspeccion mecanica obligatoria")

#Operador alternario
if antiguedad == "si":
    estado_riesgo = "Bajo Riesgo" if economia <= 800 and antiguedad == "si" else "Alto riesgo"
    print(f"El estado de riesgo de {name} es: {estado_riesgo}")
    print(f"-" * 50)
    print(f"Hola {name}, tu vehiculo {antiguedad} tiene menos de 10 años, has tenido {accidente}, y tu tarifa es de {economia}")
