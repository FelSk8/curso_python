# main.py
# Este archivo es el PROGRAMA PRINCIPAL.
# Aquí importamos y usamos las funciones que creamos en mimodulo.py

# Importamos nuestro módulo
import mimodulo

# Usamos la función holaMundo del módulo y mostramos el resultado
print(mimodulo.holaMundo("Luis"))

# Usamos la función calculadora del módulo
# Pasamos dos números y le decimos que muestre operaciones "básicas"
print(mimodulo.calculadora(3, 5, True))


# Importamos el módulo datetime (sirve para trabajar con fechas y horas)
import datetime

# Obtener la fecha actual (solo año, mes y día)
print(datetime.date.today())

# Obtener la fecha y hora actual (fecha completa con hora, minutos, segundos, microsegundos)
fecha_completa = datetime.datetime.now()

# Mostrar toda la fecha
print(fecha_completa)

# Mostrar solo el año
print(fecha_completa.year)

# Mostrar solo el mes
print(fecha_completa.month)

# Mostrar solo el día
print(fecha_completa.day)

# ----------- FORMATEAR FECHA -----------

# strftime sirve para DAR FORMATO a una fecha
# %d → día | %m → mes | %Y → año | %H:%M:%S → hora:minuto:segundo
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y")

print("Mi fecha personalizada:", fecha_personalizada)


# Importamos el módulo math (tiene funciones matemáticas avanzadas)
import math

# Calcular la raíz cuadrada de un número
print("Raiz cuadrada de 81: ", math.sqrt(81))  # → 9.0

# Constante PI
print("Numero pi: ", math.pi)  # → 3.141592653589793

# Redondear PI hacia abajo (función floor siempre baja al entero más cercano)
print("Redondear: ", math.floor(math.pi))  # → 3


# -----------------------------------------------
# Importamos el módulo random (para generar números aleatorios)
import random

# Generar un número entero aleatorio entre 15 y 52 (ambos incluidos)
print("Numero aleatorio entre 15 y 52: ", random.randint(15, 52))
