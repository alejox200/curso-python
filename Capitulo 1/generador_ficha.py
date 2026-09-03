nombre = input("Escribe tu nombre: ")
email = input("Escribe tu correo electronico: ")
telefono = input("Escribre tu numero de teléfono: ")
#La petición de datos

nombre_titulo = nombre.title().strip()
correo_limpio = email.lower().strip()
telefono_limpio = telefono.replace("-", "").replace(" ", "")
#Las limpiezas

print(f"Nombre: {nombre_titulo} y tiene la catidad de caracteres de: {len(nombre_titulo)}")
print(f"correo electronico: {correo_limpio} y tiene la catidad de caracteres de: {len(correo_limpio)}")
print(f"telefono: {telefono_limpio} y tiene la catidad de caracteres de: {len(telefono_limpio)}")
#Resultado
