#Claves
calve_secreta = "python314"

clave_usuario = input("ingresa la contraseña al servidor: ").strip()

#Practica if, else
if clave_usuario == calve_secreta:
    print("=" * 50)
    print("ACESO AUTORIZADO AL SERVIDOR")
    print("=" * 50)
else:
    print("=" * 50)
    print("ERROR: Contraseña incorrecta.")
    print("Intento registrado por seguridad.")
    print("=" * 50)
    