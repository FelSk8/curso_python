"""
Ejercicio E: Biblioteca de libros
"""

# 1. Tabla de géneros con sus libros
tabla = [
    {
        "categoria": "FANTASÍA",
        "libros": ["Harry Potter", "El Hobbit", "Narnia"]
    },
    {
        "categoria": "CIENCIA FICCIÓN",
        "libros": ["Dune", "Star Wars", "Fundación"]
    },
    {
        "categoria": "HISTORIA",
        "libros": ["Sapiens", "Los pilares de la tierra", "Historia de Roma"]
    }       
]

# 2. Recorrer la tabla y mostrarla ordenada
for genero in tabla:
    print(f"------- {genero['categoria']} -------")
    for libro in genero["libros"]:
        print(libro)
