usuario = "admin"
password_correcta = True
intentos = 3

if intentos > 0:
    if usuario == "admin" and password_correcta == True:
        print("Login Exitoso")
    else:
        print("Credenciales Incorrectas")
else:
    print("Cuenta Bloqueada")

#linea 5 el if no termina con :
#linea 6 solo contiene un "=" cuando para verificar si es igual deben ser dos
#linea 7 le falta una tabulacion en el print