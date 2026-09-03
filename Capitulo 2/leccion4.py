#Sistema de Validación de Descuento Especial
es_socio = input("¿Eres socio del club? (si/no): ").strip().lower()

if es_socio == "si":
    anios_antiguedad = int(input("¿Cuantos años llevas en el club?: "))

    if anios_antiguedad >= 10:
        categoria = "Socio VIP Platino"
        descuento = 30
    else:
        categoria = "Socio Estamdar"
        descuento = 15

    print(f"Felicidades! Perteneces a la categoría {categoria} y tienes un descuento del {descuento}%")
else:
    print("Acceso como Invitado: No tienes descuentos aplicables")

#Operador alternario para un mensaje de bienvenida
mensaje = "Bienvenido Socio" if es_socio == "no" else "Dato invalido"
print(mensaje)