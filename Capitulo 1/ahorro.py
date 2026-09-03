nombre = input("Escribe tu nombre: ")
#string
salario = float(input("Escribe tu salario mensual: "))
#float
gasto = float(input("Escribe tu gasto mensual total: "))
#float
meses = int(input("¿Cuántos meses deseas ahorrar?: "))
#int
ahorro_mensual = (salario - gasto) 
ahorro_proyectado = (ahorro_mensual * meses)

print(f"Hola {nombre}, tu ahorro mensual es de: Q{ahorro_mensual}")
print(f"En {meses} meses habrás ahorrado Q{ahorro_proyectado}")
