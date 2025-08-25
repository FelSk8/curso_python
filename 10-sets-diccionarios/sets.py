"""
SET es un tipo de dato, para tener una colección de valores,
pero no tiene ni índice ni orden.
Los sets en Python son ideales para almacenar elementos únicos,
es decir, no permite duplicados.
"""

# Definición de un conjunto (SET) llamado personas
personas = {
    "Luis",
    "Felipe",
    "Isaac"
}

# Añadir un nuevo elemento al set
personas.add("Francisco")  # Método .add() agrega un elemento al set

# Eliminar un elemento específico del set
personas.remove("Luis")    # Método .remove() elimina un elemento existente

# Mostrar el tipo de dato (confirmar que es un 'set')
print(type(personas))  # Output: <class 'set'>

# Imprimir todos los elementos del set
print(personas)  # Los elementos no tienen orden específico
