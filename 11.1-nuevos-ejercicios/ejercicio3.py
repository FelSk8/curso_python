"""
Ejercicio C: Validar dirección de correo
"""

# 1. Pedir al usuario que escriba un correo electrónico
email = input("Ingresa un correo: ")

# 2. Si el texto está vacío:
#      - Guardar "usuario@ejemplo.com"
#      - Mostrarlo en mayúsculas
if len(email.strip()) == 0:   # aquí ya basta con verificar si está vacío
    email = "usuario@ejemplo.com"
    print(email.upper())

# 3. Si el texto NO está vacío:
#      - Mostrarlo en minúsculas
else:
    print(email.lower())
