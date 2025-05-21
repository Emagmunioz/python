# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.

# Crear la lista de la compra

lista_compra = ["pan", "leche", "huevos", "manzanas", "arroz"]

# Mostrar el primer y el último elemento

print("Primer elemento:", lista_compra[0])
print("Último elemento:", lista_compra[-1])

# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.

# Lista original

lista_compra = ["pan", "leche", "huevos", "manzanas", "arroz"]

# Agregar un nuevo elemento

lista_compra.append("queso")  # añade al final

# Eliminar un elemento (por ejemplo, "leche")

lista_compra.remove("leche")  # elimina por valor

# Mostrar la lista actualizada

print("Lista actualizada:", lista_compra)

# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.

# Lista desordenada

numeros = [42, 7, 19, 3, 25, 10]

# Ordenar la lista de menor a mayor

numeros.sort()

# Mostrar la lista ordenada

print("Lista ordenada:", numeros)

# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

# Crear una tupla con latitud y longitud

coordenada = (40.4168, -3.7038)  # Ejemplo: Madrid, España

# Mostrar la tupla completa

print("Coordenada:", coordenada)

# Mostrar latitud y longitud por separado

print("Latitud:", coordenada[0])
print("Longitud:", coordenada[1])


# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.

# Crear una tupla con 3 elementos

mi_tupla = ("rojo", "verde", "azul")

# Intentar cambiar el segundo elemento

mi_tupla[1] = "amarillo"  # Esto causará un error. Las tuplas son inmutables.

# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

# Crear el diccionario

persona = {
    "nombre": "Laura",
    "edad": 28,
    "ciudad": "Barcelona"
}

# Mostrar el diccionario

print(persona)

# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.

# Diccionario original

persona = {
    "nombre": "Laura",
    "edad": 28,
    "ciudad": "Barcelona"
}

# Cambiar el valor de 'ciudad'

persona["ciudad"] = "Madrid"

# Añadir una nueva clave 'email'

persona["email"] = "laura@example.com"

# Mostrar el diccionario actualizado

print(persona)

# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.

# Diccionario actualizado

persona = {
    "nombre": "Laura",
    "edad": 28,
    "ciudad": "Madrid",
    "email": "laura@example.com"
}

# Imprimir cada clave y valor

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# ------------------------------
# SETS
# ------------------------------

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.

# Lista con nombres repetidos

nombres = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Marta"]

# Crear un set para obtener solo nombres únicos

nombres_unicos = set(nombres)

# Mostrar los nombres únicos

print("Nombres únicos:", nombres_unicos)

# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

# Usando el operador -

diferencia = A - B

print("Elementos en A pero no en B:", diferencia)

# ------------------------------
# EXTRA
# ------------------------------

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.

# Crear el diccionario con personas y sus hobbies

hobbies = {
    "Ana": ["leer", "bailar"],
    "Luis": ["fútbol", "ajedrez"],
    "Marta": ["pintar", "yoga"]
}

# Añadir un nuevo hobby a una persona (por ejemplo, a Ana)

hobbies["Ana"].append("viajar")

# Mostrar todos los hobbies de otra persona (por ejemplo, de Luis)

print("Los hobbies de Luis son:", hobbies["Luis"])
