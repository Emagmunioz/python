# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.

from collections import Counter


def analizar_texto():
    try:
        texto = input("Introduce un párrafo: ").strip()
        if not texto:
            raise ValueError("❌ El texto no puede estar vacío.")
        
        texto = texto.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
        palabras = texto.split()

        total_palabras = len(palabras)
        conteo = Counter(palabras)
        mas_repetida = conteo.most_common(1)[0]

        print(f"\n🔢 Total de palabras: {total_palabras}")
        print("\n📊 Frecuencia de palabras:")
        for palabra, cantidad in conteo.items():
            print(f"   {palabra}: {cantidad} veces")

        print(f"\n🏆 Palabra más repetida: '{mas_repetida[0]}' ({mas_repetida[1]} veces)")

    except ValueError as ve:
        print(ve)

analizar_texto()

