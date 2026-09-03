plato = "Pastel de Chocolate"
precio_plato = 120.50
#string
#float
personas = 5
#int

print(f"Tenemos {plato} para {personas} personas, el precio de {plato} es de:Q{precio_plato}")

subtotal = (precio_plato * personas)
propina = (subtotal * 0.10)

print(f"Propina del 10%: {propina} y el total final es: {subtotal + propina}")

