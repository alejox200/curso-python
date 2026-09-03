#El primer error es es la aliniacion de los if, ya que el segundo no tiene los dos tabs necesarios y no se sabra que else pertenece al primer if o al segundo
#Falta una valiable llamada edad
nivel = input("Ingrese su rango (admin, usuario, invitado): ").strip().lower()
edad = int(input("Ingrese su edad: "))

if nivel == "admin": autenticado = True

if autenticado:
    if nivel == "admin":
        print("Acceso Total")
    else:
        print("Acceso Limitado")
else:
    print("No autenticado")

tipo = "Mayor" if edad >= 18 else "Menor"
print(tipo)
#Mejore un poco el progrema
