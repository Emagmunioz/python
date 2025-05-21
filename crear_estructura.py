"""
Script: crear_estructura.py
Crea automáticamente una estructura básica de un proyecto Python profesional.
Como usarlo:
    python crear_estructura.py NombreDelProyecto
"""

import os
from pathlib import Path  # Para manejar rutas de forma multiplataforma
import subprocess  # Para ejecutar comandos como la creación del entorno virtual
import sys  # Para leer argumentos desde la línea de comandos

# 📥 1. Obtenemos el nombre del proyecto desde argumentos 
# Si el usuario no proporciona un nombre, usamos "MiProyecto" por defecto
# Si se proporciona un nombre, lo usamo
nombre_proyecto = sys.argv[1] if len(sys.argv) > 1 else "MiProyecto"

# 📁 2. Definimos las rutas base
# Usamos la ruta actual del script como base para el proyecto
# y creamos las carpetas src y tests dentro de ella
base = Path(nombre_proyecto)
src = base / "src"
tests = base / "tests"

# 📂 3. Creamos carpetas del proyecto
# Creamos la carpeta base y las subcarpetas src y tests
# Si ya existen, no se crean de nuevo
(src).mkdir(parents=True, exist_ok=True)
(tests).mkdir(parents=True, exist_ok=True)

# 📄 4. Creamos archivos importantes con contenido inicial
# Creamos un archivo .gitignore para ignorar archivos innecesarios
# y un README.md con el nombre del proyecto
# También creamos un requirements.txt vacío y un main.py con un mensaje de bienvenida
# y un test básico en test_main.py
(base / ".gitignore").write_text("venv/\n__pycache__/\n*.pyc\n")
(base / "README.md").write_text(f"# {nombre_proyecto}\n\nProyecto básico de Python.")
(base / "requirements.txt").write_text("")
(src / "main.py").write_text('print("Hola desde main.py")\n')
(tests / "test_main.py").write_text("def test_example():\n    assert 1 + 1 == 2\n")

# 🐍 5. Creamos un entorno virtual dentro de la carpeta del proyecto
# Usamos subprocess para ejecutar el comando de creación del entorno virtual
# Esto permite que el script funcione en diferentes sistemas operativo
subprocess.run(["python", "-m", "venv", "venv"], cwd=base)

# ✅ 6. Mensaje de confirmación
print(f"✅ Proyecto '{nombre_proyecto}' creado correctamente.")
print("➡️  Activa el entorno con:")
print(f"   cd {nombre_proyecto}")
print("   .\venv\Scripts\Activate.ps1  # en PowerShell (Windows)")
print("   source venv/bin/activate       # en Mac/Linux")
