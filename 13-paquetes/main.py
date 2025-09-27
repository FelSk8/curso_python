print("PROBANDO PAQUETES:")

# Importamos submódulos desde un paquete llamado "mipaquete"
# Un paquete es una carpeta que contiene varios módulos (archivos .py) y un archivo __init__.py
from mipaquete import pruebas
from mipaquete import herramientas

# Llamamos a una función dentro del módulo "pruebas.py"
pruebas.probando()  

# Llamamos a una función dentro del módulo "herramientas.py"
herramientas.nombreCompleto("Luis", "Guzman")
