mensaje = "      bienvenido al curso de Python de backend      "
#1. Quitar los espacios sobrantes con la funcion .strip()
mensaje_limpio = mensaje.strip()
#2. Poner en formato de titulo con la funcion .title()
mensaje_titulo = mensaje_limpio.title()
#3. Reemplazar una palabra con la funcion .replace()
mensaje_modificado = mensaje_titulo.replace("Python","Python 3.14")

print(f"Texto procesado: {mensaje_modificado}")
print(f"Longitud total: {len(mensaje_modificado)}")
