import os
import json

# Ruta absoluta del archivo kaggle.json en la misma carpeta del script
script_dir = os.path.dirname(__file__)
kaggle_path = os.path.join(script_dir, "kaggle.json")

with open(kaggle_path) as f:
    kaggle_token = json.load(f)

