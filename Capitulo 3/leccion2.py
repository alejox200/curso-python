#Analizador de caracteres y conteo de vocales
palabra = input("Ingresa una palabra para analizar: ").strip().lower()

total_vocales = 0

print("--Deletrando la palabra--")

for caracter in palabra:
    print(f"Caracter: {caracter}")
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        total_vocales += 1

print("=" * 50)
print(f"La palabra '{palabra}' tiene {total_vocales} vocales.")
