# Ejercicio 6: Comprobador de contraseñas seguras
# ------------------------------------------------
# Pide una contraseña al usuario.
# Valida que:
# - Tiene al menos 8 caracteres
# - Contiene mayúsculas, minúsculas y números
# 💡 Usa raise y excepciones personalizadas con mensajes explicativos.


def comprobar_contraseña(contraseña):
    if len(contraseña) < 8:
        raise ValueError("❌ La contraseña debe tener al menos 8 caracteres.")
    
    if not any(c.islower() for c in contraseña):
        raise ValueError("❌ La contraseña debe contener al menos una letra minúscula.")
    
    if not any(c.isupper() for c in contraseña):
        raise ValueError("❌ La contraseña debe contener al menos una letra mayúscula.")
    
    if not any(c.isdigit() for c in contraseña):
        raise ValueError("❌ La contraseña debe contener al menos un número.")

    print("✅ Contraseña válida y segura.")

def solicitar_contraseña():
    contraseña = input("Introduce una contraseña: ").strip()
    try:
        comprobar_contraseña(contraseña)
    except ValueError as error:
        print(error)

solicitar_contraseña()
