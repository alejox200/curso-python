#Datos
total_pagar = 0.0
cantidad_articulos = 0

while True:
    print("\n" + "*" * 50)
    print("SUPERMERCADO ABARROTES")
    precio = float(input("Ingresa el precio del artículo: "))
    total = total_pagar + precio
    cantidad_articulos += 1

    agregar = input("¿Deseas agregar otro artículo? (s/n): ").strip().lower()
    if agregar != "s" and agregar != "n":
        print("Opción inválida, por favor intenta de nuevo.")
        continue
    elif agregar == "s":
        precio = float(input("Ingresa el precio del artículo: "))
        total = total_pagar + precio
        cantidad_articulos += 1
        continue
    elif agregar == "n":
        print("¿Qué deseas hacer ahora?")

    print("-" * 50)
    print("OPCIONES:")
    print("1. Pagar")
    print("2. Cancelar")
    print("3. Salir del programa")
    opcion = input("Selecciona una opción(1-2): ").strip()

    if opcion == "3":
        print("Saliendo del programa...")
        break
   
    if  opcion != "1" and opcion != "2":
        print("Opción inválida, por favor intenta de nuevo.")
        continue

    if opcion == "2":
        print("Compra cancelada.")
        total = 0.0
        cantidad_articulos = 0
        continue

    if precio <= 0:
        print("El precio es invalido.")
        continue

    elif opcion == "1":
        if cantidad_articulos == 0:
            print("No has agregado ningun artículo.")
        elif cantidad_articulos > 0:
            print("Total a pagar: ", total)
            print("Gracias por su compra.")
            break               

#Agente Ternario
print("-" * 50)
print("TU COMPRA:")
print("-" * 50)
print(f"Tu cantidad de articulos: {cantidad_articulos:.2f}")
print(f"Tu total a pagar es: ${total:.2f}")

print("\n" + "*" * 50)
