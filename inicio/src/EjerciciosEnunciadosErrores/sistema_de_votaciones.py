# Ejercicio 1: Sistema de votaciones
# -----------------------------------
# Crea un programa en consola con las siguientes opciones:
# 1. Añadir película
# 2. Votar por una película
# 3. Mostrar resultados
# 4. Salir
# Si se intenta votar por una película no registrada, muestra error (usa try/except con KeyError).
# Usa funciones separadas por funcionalidad.
# (Bonus: guardar votos en un fichero CSV)
import csv

peliculas = {}

def añadir_pelicula():
    nombre = input("Nombre de la película: ").strip()
    if nombre in peliculas:
        print("⚠️ La película ya está registrada.")
    else:
        peliculas[nombre] = 0
        print(f"✅ Película '{nombre}' añadida.")

def votar_pelicula():
    nombre = input("¿Por qué película quieres votar? ").strip()
    try:
        peliculas[nombre] += 1
        print(f"🗳️ Voto registrado para '{nombre}'")
    except KeyError:
        print("❌ Error: La película no está registrada.")

def mostrar_resultados():
    if not peliculas:
        print("📭 No hay películas registradas.")
        return
    print("\n📊 Resultados:")
    for nombre, votos in peliculas.items():
        print(f"🎬 {nombre}: {votos} votos")

def guardar_en_csv():
    with open("votos_peliculas.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Película", "Votos"])
        for nombre, votos in peliculas.items():
            writer.writerow([nombre, votos])
    print("📁 Resultados guardados en 'votos_peliculas.csv'.")

def mostrar_menu():
    print("\n🎥 MENÚ:")
    print("1. Añadir película")
    print("2. Votar por una película")
    print("3. Mostrar resultados")
    print("4. Salir")

def programa():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")
        if opcion == "1":
            añadir_pelicula()
        elif opcion == "2":
            votar_pelicula()
        elif opcion == "3":
            mostrar_resultados()
        elif opcion == "4":
            guardar_en_csv()
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❗ Opción no válida. Intenta de nuevo.")

programa()
