#Datos
print("***Bienvenido al Simulador de Depósitos***")
print("-" * 40)

saldo_actual = 0.0
meta_ahorro = 1000.0
total_depositos = 0

#Bucle While
while saldo_actual < meta_ahorro:
    print(f"Saldo actual: ${saldo_actual:.2f} | Meta: ${meta_ahorro:.2f}")
    print(f"Te faltan ${(meta_ahorro - saldo_actual):.2f} para alcanzar la meta")
    deposito = float(input("¿Cuanto deseas depositar?: $"))
    if deposito > 0:
        saldo_actual += deposito
        total_depositos += 1
        print(f"Depósito # {total_depositos}: ${deposito}")
    else:
        print("Error: Monto invalido, porfavor intente de nuevo")

print("-" * 40)
print(f"🎉 ¡FELICIDADES! Has alcanzado tu meta de ahorro de ${meta_ahorro} en {total_depositos} depósitos.")
print(f"Saldo final: ${saldo_actual}")
print("-" * 40)
