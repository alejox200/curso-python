#Sistema de Acceso a Evento Exclusivo
edad= int(input("Ingresa tu edad: "))
tiene_boleto = input("¿Tienes boleta? (si/no): ").strip().lower()
vip = input("¿Eres VIP? (si/no): ").strip().lower()

#Convertimos las respuestas a booleanos
posee_entrada = (tiene_boleto == "si")
es_vip = (vip == "si")

#Condición compuesta con and y or
if edad >= 18 and (posee_entrada or es_vip):
    print("=" * 50)
    print("🎊 ¡Bienvenido al evento! Acceso concedido")
else:
    print("=" * 50)
    print("❌ Acceso Denegado: Debes ser mayor de 18 años y tener entrada o ser VIP")
    print("=" * 50)