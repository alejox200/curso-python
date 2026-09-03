#Datos 
name = input("Ingresa tu nombre: ").strip().lower()
total = float(input("Ingresa tu monto de tu compra: "))

#Procesamiento
if total >= 1000:
    print("=" * 50)
    print(f"😄 FELICIDADES {name}! Tienes un descuento del 20%")
    print(f"Tu monto inicial es: ${total}")
    print(f"El descuento es: ${total * 0.20}")
    print(f"Tu monto final es: ${total - (total * 0.20)}")
    print("=" * 50)
elif total >= 500:
    print("=" * 50)
    print(f"😄 FELICIDADES {name}! Tienes un descuento del 10%")
    print(f"Tu monto inicial es: ${total}")
    print(f"El descuento es: ${total * 0.10}")
    print(f"Tu monto final es: ${total - (total * 0.10)}")
    print("=" * 50)
elif total >= 200:
    print("=" * 50)
    print(f"😄 FELICIDADES {name}! Tienes un descuento del 5%")
    print(f"Tu monto inicial es: ${total}")
    print(f"El descuento es: ${total * 0.05}")
    print(f"Tu monto final es: ${total - (total * 0.05)}")
    print("=" * 50)
else:
    print("=" * 50)
    print(f"Lo siento {name}, no tienes descuento")
    print(f"El descuento es: $0")
    print("=" * 50)
    
print("=" * 50)
print(f"GRACIAS POR SU COMPRA {name}")
print("=" * 50)
