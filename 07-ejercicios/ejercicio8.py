# Ejercicio 8: Calcular cuánto es X por ciento de un número

# Pedimos al usuario un número y lo convertimos a entero
numero = int(input("Introduce el número: "))

# Pedimos al usuario el porcentaje que quiere calcular y lo convertimos a entero
porcentaje = int(input(f"¿Qué porcentaje quieres sacar de {numero}? : "))

# Realizamos la operación para calcular el porcentaje
# Fórmula: (número * porcentaje) / 100
operacion = numero * (porcentaje / 100)

# Mostramos el resultado en pantalla usando f-strings
print(f"El {porcentaje}% de {numero} es: {operacion}")
