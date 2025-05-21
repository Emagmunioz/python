# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type() para imprimir qué tipo de dato es cada una:
# a = "Hola"
# b = 25
# c = 3.14
# d = True
# e = None

# Declaración de variables
a = "Hola"
b = 25
c = 3.14
d = True
e = None

# Mostrar el tipo de cada variable

print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'NoneType'>

# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"

# Conversión de cadena a número y suma

numero = int("42")  # convierte la cadena "42" en entero
resultado = numero + 8
print(resultado)  # Muestra: 50

# Conversión de número a cadena y concatenación en una frase

puntuacion = str(100)  # convierte el número 100 en cadena
mensaje = "Tu puntuación final es: " + puntuacion
print(mensaje)  # Muestra: Tu puntuación final es: 100

# ------------------------------
# VARIABLES
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.

# Declaración de variables

nombre = "Eva"
edad = 53

# Imprimir el saludo

print("Hola, me llamo", nombre, "y tengo", edad, "años.")


# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
# x = "gato"
# y = "perro"
# Intercambia sus valores para que x valga "perro" y y valga "gato".

# Variables iniciales

x = "gato"
y = "perro"

# Intercambio de valores

x, y = y, x

# Mostrar los nuevos valores

print("x =", x)  # x = perro
print("y =", y)  # y = gato

# ------------------------------
# OPERADORES
# ------------------------------

# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:
# pan = 1.50
# leche = 1.24
# huevos = 2.70
# Calcula el total y muestra: “El total de tu compra es de: 4,25€”

# Precios de los productos

pan = 1.50
leche = 1.24
huevos = 2.70

# Calcular el total

total = pan + leche + huevos

# Mostrar el total formateado con dos decimales

print(f"El total de tu compra es de: {total:.2f}€")

# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.

# Pedir un número al usuario

numero = int(input("Introduce un número: "))

# Comprobar si es par o impar

if numero % 2 == 0:
    print("Es un número par.")
else:
    print("Es un número impar.")

# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------

# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.

# Pedir la edad al usuario

edad = int(input("Introduce tu edad: "))

# Comprobar si es mayor de edad

if edad >= 18:
    print("Puedes entrar.")
else:
    print("Acceso denegado.")

# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.

# Mostrar opciones

print("Elige una opción:")
print("1. Ver perfil")
print("2. Editar perfil")
print("3. Cerrar sesión")

# Leer la opción del usuario

opcion = input("Introduce el número de tu elección: ")

# Mostrar mensaje según la opción

if opcion == "1":
    print("Mostrando tu perfil...")
elif opcion == "2":
    print("Abriendo el editor de perfil...")
elif opcion == "3":
    print("Cerrando sesión. ¡Hasta luego!")
else:
    print("Opción no válida.")

# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------

# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().

entrada = input("Escribe algo: ")

# Intentar detectar el tipo de dato

try:
    valor = int(entrada)
    print("Has escrito un número entero.")
except ValueError:
    try:
        valor = float(entrada)
        print("Has escrito un número decimal.")
    except ValueError:
        if entrada.strip():  # Si no está vacío ni son solo espacios
            print("Parece que es una cadena de texto.")
        else:
            print("No sé qué es esto 😵‍💫")

# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.

# Pedir dos números al usuario

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostrar el menú de opciones

print("\nElige una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Leer la opción

opcion = input("Introduce el número de la operación: ")

# Realizar la operación según la opción elegida

if opcion == "1":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif opcion == "4":
    if num2 == 0:
        print("No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
else:
    print("Opción no válida.")

# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”

# Pedir la edad al usuario

edad = int(input("Introduce tu edad: "))

# Clasificar según la edad

if edad < 3:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Infancia")
elif 13 <= edad <= 17:
    print("Adolescencia")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 100:
    print("Senior")
else:
    print("Edad fuera de rango considerado.")
