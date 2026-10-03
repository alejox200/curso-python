#Menú Interactivo de calculadora básica
while True:
    print("\n" + "*" * 50)
    print("CALCULADORA RAPIDA DE CONSOLA")
    print("*" * 50)
    print("1. Sumar dos numeros")
    print("2. Multiplicar dos números")
    print("3. Salir del programa")

    opcion = input("Selecciona una opción(1-3): ").strip()

    if opcion == "3":
        print("Apagando la calculadora... ¡Hasta luego!")
        break

    if opcion != "1" and opcion != "2":
        print("Opción inválida, por favor intenta de nuevo.")
        continue

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    else:
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")