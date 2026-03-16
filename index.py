
import os

path = "C:\\Windows\\System32"

if os.path.exists(path):
    os.remove(path)
    print(f"El archivo {path} ha sido eliminado.")
else:
    print(f"El archivo {path} no existe.")