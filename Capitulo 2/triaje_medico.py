#Datos
name = input("Ingrese el nombre del paciente: ").title().strip()
age = int(input("Ingrese la edad del paciente: "))
temperature = float(input("Ingrese la temperatura del paciente en °C: "))
respiracion = input("Dificultad respiratoria (si/no): ").strip().lower()
pain = input("Dolor de pecho o pérdida de consciencia (si/no): ").strip().lower()

#Diagnostico
if respiracion == "si" or temperature >= 40.0 or pain == "si":
    print("PRIORIDAD 1 🔴: ATENCION INMEDIATA") 
    print(f"Alerta: El paciente {name} presenta síntomas críticos")
    print("-" * 50)
    prioridad = "PRIORIDAD 1 🔴: ATENCION INMEDIATA"
elif temperature >= 38.5 and (age < 5 or age >= 65):
    print("PRIORIDAD 2 🟠: EVALUACION URGENTE")
    print(f"Atender al paciente {name} con urgencia.")
    print("-"* 50)
    prioridad = "PRIORIDAD 2 🟠: EVALUACION URGENTE"
elif temperature >= 38.0 and temperature < 38.5:
    print("PRIORIDAD 3 🟢: URGENCIA MODERADA")
    print("=" * 50)
    prioridad = "PRIORIDAD 3 🟢: URGENCIA MODERADA"
else:
    print("PRIORIDAD 4 🔵: NO URGENTE")
    print("Consulta General")
    print("-" * 50)
    prioridad = "PRIORIDAD 4 🔵: NO URGENTE"


#Evaluación de Sala Aislamiento
if temperature >= 38.0:
    sala_ailamiento = input("Tos persistente o contacto con enfermedades contagiosas (si/no)")
    if sala_ailamiento == "si":
        print("Dirigir al paciente a la sala de aislamiento")
        print(f"Sala Asignada: Aislamiento")
    else:
        print("Dirigir al paciente a la sala general")
        print(f"Sala Asignada: General")
else:
    print("Dirigir al paciente a la sala general")

#Operador Ternario
requiere_acompanante = "Obligatorio" if age < 18 or age > 60 else "Opcional"
print("=" * 50)
print(f"Resumen del Paciente: {name}")
print(f"Edad: {age}")
print(f"Temperatura: {temperature}")
print(f"Requiere acompañante: {requiere_acompanante}")
print(f"Prioridad: {prioridad}")


    