nombre = input("Escribe tu nombre: ")
#input en valor str
nacimiento = int(input("Escribe tu año de nacimiento: "))
#input en valor int

año_actual = 2026
edad_calculada = año_actual - nacimiento

print(f"Hola {nombre}, en el año {año_actual} tendrás {edad_calculada} años aproximadamente.")
