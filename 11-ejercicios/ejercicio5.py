"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA              DEPORTE
GTA         ASSINS                FIFA 25  
COD         CRASH                 PES 25  
PUGB        PRINCE OF PERSIA      MOTO GP 25

MOSTRAR ESTA INFORMACION ORDENADA 
"""

# Creamos una lista de diccionarios. Cada diccionario tiene:
# - Una categoría (ACCION, AVENTURA, DEPORTE)
# - Una lista de juegos relacionados
tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSINS", "CRASH", "PRINCE OF PERSIA"]
    },
    {
        "categoria": "DEPORTE",
        "juegos": ["FIFA 25", "PES 25", "MOTO GP 25"]
    }       
]

# Recorremos cada diccionario de la lista (cada categoría)
for categoria in tabla:
    # Mostramos el título de la categoría
    print(f"---------- {categoria['categoria']} ----------")
    
    # Recorremos la lista de juegos y los mostramos uno por uno
    for juego in categoria["juegos"]:
        print(juego)
