# 🌟 Reto Extra: Simulador de reservas de hotel
# ----------------------------------------------
# Habitaciones del 101 al 110. El usuario puede:
# 1. Ver habitaciones disponibles
# 2. Reservar habitación (introduciendo su nombre)
# 3. Cancelar reserva
# 4. Ver reservas confirmadas
# 5. Salir
# Las reservas se almacenan en un diccionario {habitacion: nombre}
# Usa funciones y control de errores con KeyError si la habitación no existe.
# (Bonus: mostrar mapa visual, reservas múltiples, carga inicial aleatoria)
import random

habitaciones = {num: None for num in range(101, 111)}

nombres_ejemplo = ["Lucía", "Carlos", "Marta", "Ana", "David"]
for _ in range(random.randint(1, 5)):
    habitacion = random.choice(list(habitaciones.keys()))
    if habitaciones[habitacion] is None:
        habitaciones[habitacion] = random.choice(nombres_ejemplo)

def mostrar_mapa():
    print("\n🗺️ Mapa de habitaciones:")
    for num in sorted(habitaciones.keys()):
        estado = "Libre" if habitaciones[num] is None else f"Ocupada por {habitaciones[num]}"
        print(f" - Habitación {num}: {estado}")

def ver_disponibles():
    disponibles = [num for num, cliente in habitaciones.items() if cliente is None]
    if disponibles:
        print("\n✅ Habitaciones disponibles:", disponibles)
    else:
        print("\n🚫 No hay habitaciones disponibles.")

def reservar():
    try:
        nombre = input("Tu nombre: ").strip()
        cantidad = int(input("¿Cuántas habitaciones deseas reservar? (1-3): "))
        if cantidad < 1 or cantidad > 3:
            raise ValueError("Puedes reservar entre 1 y 3 habitaciones.")
        disponibles = [num for num, cliente in habitaciones.items() if cliente is None]
        if len(disponibles) < cantidad:
            print("❌ No hay suficientes habitaciones disponibles.")
            return
        for i in range(cantidad):
            mostrar_mapa()
            hab = int(input(f"Elige habitación disponible #{i+1}: "))
            if hab not in habitaciones:
                raise KeyError("La habitación no existe.")
            if habitaciones[hab] is not None:
                print(f"⚠️ La habitación {hab} ya está ocupada.")
            else:
                habitaciones[hab] = nombre
                print(f"🛏️ Habitación {hab} reservada para {nombre}.")
    except ValueError as ve:
        print("❌", ve)
    except KeyError as ke:
        print("❌", ke)

def cancelar():
    try:
        hab = int(input("Introduce el número de la habitación a cancelar: "))
        if hab not in habitaciones:
            raise KeyError("La habitación no existe.")
        if habitaciones[hab] is None:
            print("⚠️ Esa habitación ya está libre.")
        else:
            print(f"🧹 Reserva de '{habitaciones[hab]}' en habitación {hab} cancelada.")
            habitaciones[hab] = None
    except ValueError:
        print("❌ Entrada inválida. Debes introducir un número.")
    except KeyError as ke:
        print("❌", ke)

def ver_reservas():
    print("\n📋 Reservas confirmadas:")
    alguna = False
    for hab, nombre in sorted(habitaciones.items()):
        if nombre:
            print(f" - Habitación {hab}: {nombre}")
            alguna = True
    if not alguna:
        print("📭 No hay reservas activas.")

def mostrar_menu():
    print("\n🏨 MENÚ DE RESERVAS")
    print("1. Ver habitaciones disponibles")
    print("2. Reservar habitación")
    print("3. Cancelar reserva")
    print("4. Ver reservas confirmadas")
    print("5. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        if opcion == "1":
            ver_disponibles()
        elif opcion == "2":
            reservar()
        elif opcion == "3":
            cancelar()
        elif opcion == "4":
            ver_reservas()
        elif opcion == "5":
            print("👋 Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("❗ Opción no válida.")

ejecutar()
