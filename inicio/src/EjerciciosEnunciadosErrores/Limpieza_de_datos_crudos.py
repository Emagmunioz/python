# Ejercicio 2: Limpieza de datos crudos
# -------------------------------------
# Dada una lista de nombres con errores (espacios, mayúsculas, duplicados),
# crea una función que la limpie devolviendo una lista ordenada y sin duplicados.
# Todos los nombres deben tener solo la primera letra en mayúscula.
# Muestra cuántos nombres únicos hay.
# 💡 Añade manejo de errores si algún elemento no es una cadena (TypeError o AttributeError)
# ✨ Ejercicio 2: Limpieza de datos crudos

def limpiar_nombres(lista_cruda):
    nombres_limpios = set()  

    for item in lista_cruda:
        try:
            nombre = item.strip().capitalize()
            nombres_limpios.add(nombre)
        except (AttributeError, TypeError):
            print(f"⚠️ Error: '{item}' no es un nombre válido. Se omitirá.")

    lista_final = sorted(nombres_limpios)
    print(f"✅ Se encontraron {len(lista_final)} nombres únicos.")
    return lista_final


nombres_crudos = [" ana ", "JUAN", "maria", "Ana", "juan ", "Carlos", 123, None, "   MARIA  "]
nombres_limpios = limpiar_nombres(nombres_crudos)
print("🔍 Nombres limpios:", nombres_limpios)