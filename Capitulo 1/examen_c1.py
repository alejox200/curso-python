#Datos
name = input("Hola, ¿Cuál es tu nombre?: ").title().strip()
coffee = input("¿Qué tipo de café quieres comprar: ").title().strip()
kg = int(input("¿Cuántos kilogramos de café quieres?: "))

#Procesamiento
bolsas = int(500)
total = kg // bolsas
residuos = kg % bolsas

#Resultados
print(f"Hola, {name}, tu pedido de {coffee} ya esta listo!!!")
print(f"-" * 50)
print(f"Has pedido {kg} kilogramos y con eso son {total} bolsas de {coffee}")
print(f"Quedan {residuos} gramos para la siguiente bolsa")

