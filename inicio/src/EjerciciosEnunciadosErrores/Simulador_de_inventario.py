# Ejercicio 4: Simulador de inventario
# -------------------------------------
# Crea un sistema que permita gestionar productos en un inventario.
# Cada producto tiene nombre, stock y precio.
# Opciones:
# 1. Añadir producto
# 2. Actualizar stock
# 3. Eliminar producto
# 4. Ver inventario
# 💡 Usa try/except para validar entradas numéricas y para controlar si el producto no existe.
# ✨ Ejercicio 4: Simulador de inventario

inventario = {}

def añadir_producto():
    nombre = input("Nombre del producto: ").strip()
    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        inventario[nombre] = {"precio": precio, "stock": stock}
        print(f"✅ Producto '{nombre}' añadido al inventario.")
    except ValueError:
        print("❌ Error: El precio y el stock deben ser valores numéricos.")

def actualizar_stock():
    nombre = input("Nombre del producto a actualizar: ").strip()
    try:
        if nombre not in inventario:
            raise KeyError
        nuevo_stock = int(input("Nuevo stock: "))
        inventario[nombre]["stock"] = nuevo_stock
        print(f"🔄 Stock de '{nombre}' actualizado a {nuevo_stock}.")
    except ValueError:
        print("❌ Error: El stock debe ser un número entero.")
    except KeyError:
        print("❌ Error: El producto no existe en el inventario.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip()
    try:
        del inventario[nombre]
        print(f"🗑️ Producto '{nombre}' eliminado.")
    except KeyError:
        print("❌ Error: El producto no existe en el inventario.")

def ver_inventario():
    if not inventario:
        print("📭 Inventario vacío.")
        return
    print("\n📦 Inventario actual:")
    for nombre, datos in inventario.items():
        print(f"- {nombre}: {datos['stock']} unidades | ${datos['precio']:.2f}")

def mostrar_menu():
    print("\n📋 MENÚ DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Actualizar stock")
    print("3. Eliminar producto")
    print("4. Ver inventario")
    print("5. Salir")

def programa_inventario():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            ver_inventario()
        elif opcion == "5":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❗ Opción no válida. Intenta de nuevo.")

programa_inventario()
