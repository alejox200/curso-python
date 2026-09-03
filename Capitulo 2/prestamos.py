#Datos
print("Bienvenido al sistema de prestamos")
print("=" * 50)
name = input("Ingresa tu nombre: ").strip().lower()
ingreso_mensual = float(input("Ingesa tu ingreso mensual: Q"))
age = int(input("Ingresa tu edad: "))
deudas = input("Tienes deudas activas (si/no): ").strip().lower()
fiador = input("¿Tienes un fiador disponible? (si/no): ").strip().lower()

#Reglas de Aprovación
if age >= 21 and age <=65 and (ingreso_mensual >= 4000) and (deudas == "no" or fiador == "si"):
    print(f"{name} Cumple con el requisito de edad")
    print("Tu solicitud de prestamo ha sido aprobada")
    print(f"Tus datos son: {name}, {ingreso_mensual}, {age}, {deudas}, {fiador}")  
    print("Felicidades entraste al programa de prestamos")
    print("=" * 50)
else:
    print(f"{name} RECHAZADO")
    print("No cumples con los requisitos")
    print("Prueba de nuevo más tarde")
    print("=" * 50)
