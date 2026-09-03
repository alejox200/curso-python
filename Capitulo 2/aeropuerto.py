#Datos iniciales
name = input("Ingresa tu nombre: ").strip().title()
peso = float(input("Ingresa el peso de tu maleta en kg: "))

#Procesamiento
if peso <= 23.0:
    print("-" * 50)
    print("su maleta esta dentro del peso permitido: ", peso)
    print("Perfecto, puedes continuar.")
    print("-" * 50)
else:
    peso_maleta = peso - 23.0
    print("-" * 50)
    print(f"ALERTA: {name}, su maleta excede el peso permitido de 23 kg, debe pagar el exceso de {peso_maleta} kg")
    print("-" * 50)

#Final
print("¡Gracias por volar con nosotros!")
print("=" * 50)
