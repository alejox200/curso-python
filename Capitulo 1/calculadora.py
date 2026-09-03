#Fase de bienvenida
name = input("Hola, danos tu nombre: ").strip().title()
title_session = input("¿Qué tema vamos a trabajar hoy?: ").strip().upper()

print(f"Hola {name}, tu clase de {title_session} ha comenzado")
print(f"Tu nombre tiene {len(name)} letras")
print("=" * 50)

#Fase de Números
number_1 = float(input("Dime el primer número: "))
number_2 = float(input("Dime el segundo número: "))

#Fase de Procesamiento Matematico
suma = number_1 + number_2
resta = number_1 - number_2
multiplicacion = number_1 * number_2
division_real = number_1 / number_2
division_entera = number_1 // number_2
residuo = number_1 % number_2
potencia = number_1 ** number_2

#Fase de Resultados
print(title_session)
print(f"-" * 50)
print(f"Hola de nuevo {name}, segun los numeros que nos diste... {number_1} y {number_2}, los resultados son:")
print("-" * 50)
print(f"La suma de {number_1} y {number_2} es igual a {suma}")
print(f"La resta de {number_1} y {number_2} es igual a {resta}")
print(f"La multiplicacion de {number_1} y {number_2} es igual a {multiplicacion}")
print(f"La division real de {number_1} y {number_2} es igual a {division_real}")
print(f"La division entera de {number_1} y {number_2} es igual a {division_entera}")
print(f"El residuo de {number_1} y {number_2} es igual a {residuo}")
print(f"La potencia de {number_1} y {number_2} es igual a {potencia}")
print("=" * 50)
print("FIN DEL PROGRAMA")