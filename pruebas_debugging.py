contador = 1

while contador <= 5:
    if contador == 3:
        continue
    print(f"Número: {contador}")
    contador += 1
#Se queda en un bucle infinito porque no hay ningun valor que lo pare ya que se salta el contador
#El contador tiene que ser agregado antes del continue para tomarse en cuenta 
