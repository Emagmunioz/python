# Ejercicio 5: Generador de alias seguro
# ---------------------------------------
# Pide al usuario nombre y apellido, y genera un alias así:
# - 3 letras del apellido (mayúsculas)
# - 2 letras del nombre (minúsculas)
# - número aleatorio del 10 al 99
# - símbolo especial aleatorio
# 💡 Valida que el nombre y apellido tengan longitud suficiente (ValueError)
import random
import string


def generar_alias():
    try:
        nombre = input("Introduce tu nombre: ").strip()
        apellido = input("Introduce tu apellido: ").strip()

        if len(nombre) < 2 or len(apellido) < 3:
            raise ValueError("❌ El nombre debe tener al menos 2 letras y el apellido al menos 3.")

        parte_apellido = apellido[:3].upper()
        parte_nombre = nombre[:2].lower()
        numero = random.randint(10, 99)
        simbolo = random.choice("!@#$%&*")

        alias = parte_apellido + parte_nombre + str(numero) + simbolo
        print(f"✅ Alias generado: {alias}")

    except ValueError as ve:
        print(ve)


generar_alias()
