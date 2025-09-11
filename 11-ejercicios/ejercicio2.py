"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
extra: Usar while y for
"""

# Creamos una lista vacía donde vamos a ir guardando elementos
coleccion = []

# --- Bucle FOR ---
# Usamos un bucle for que va desde 0 hasta 119 (120 números en total)
for contador in range(0, 120):
    # .append() sirve para AGREGAR un elemento nuevo al final de la lista
    coleccion.append(f"elemento-{contador}")
    
    # Mostramos el elemento recién añadido
    print("Mostrar con for: " + coleccion[contador])

# Mostramos toda la lista al final del bucle
print(coleccion)


# --- Bucle WHILE ---
# Reiniciamos el contador
contador = 0

# Mientras el contador sea menor o igual a 120, seguimos repitiendo
while contador <= 120:
     # Usamos append() nuevamente para agregar un nuevo elemento al final de la lista
     coleccion.append(f"elemento-{contador}")
     
     # Mostramos el elemento recién añadido
     print("Mostrar - con while - : " + coleccion[contador])
     
     # Aumentamos el contador en 1 para que el bucle no sea infinito
     contador = contador + 1

# Mostramos la lista final después de llenar con while
print(coleccion)
