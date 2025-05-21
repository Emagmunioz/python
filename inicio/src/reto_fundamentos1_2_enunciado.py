# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.
#    - Guarda el contacto en una lista como un diccionario.

# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo

# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir

# Lista para almacenar los contactos

contactos = []

def añadir_contacto():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")
    contacto = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    contactos.append(contacto)
    print(f"✅ Contacto de {nombre} añadido.")

def mostrar_contactos():
    if not contactos:
        print("📭 No hay contactos guardados.")
    else:
        for c in contactos:
            print(f"Nombre: {c['nombre']} – Edad: {c['edad']} – Ciudad: {c['ciudad']}")

def buscar_contacto():
    nombre_buscar = input("Introduce el nombre a buscar: ")
    encontrados = [c for c in contactos if c["nombre"].lower() == nombre_buscar.lower()]
    if encontrados:
        for c in encontrados:
            print(f"📇 Encontrado: Nombre: {c['nombre']} – Edad: {c['edad']} – Ciudad: {c['ciudad']}")
    else:
        print("❌ Contacto no encontrado.")

# Bucle principal

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Buscar por nombre")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        añadir_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❗ Opción no válida. Intenta de nuevo.")
