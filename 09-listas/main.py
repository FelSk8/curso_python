"""
Listas (Arrays)
Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice numérico.
"""

# Variable simple
pelicula = "Batman"

# Definir lista con corchetes
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]

# Crear lista con la función list() a partir de una tupla
cantantes = list(('Dj Isaac', 'Dj Cooner', 'Dj Malice'))

# Crear lista con valores numéricos usando range()
years = list(range(2020, 2050))  # Genera los números del 2020 al 2049

# Lista con datos variados (string, entero, float, booleano)
variada = ["Luis", 30, 5.5, True, "Chile"]

# Imprimir listas en pantalla
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

#Indice

# Cambiar el valor en la posición 1 (índice 1)
peliculas[1] = "Dragon ball"

# Mostrar toda la lista
print(peliculas)

# Mostrar el elemento en la posición 1
print(peliculas[1])

# Mostrar el elemento en la posición -2 (segundo desde el final)
print(peliculas[-2])

# Mostrar un rango: desde el índice 0 hasta el índice 1 (sin incluir el 2)
print(cantantes[0:2])

# Mostrar desde el índice 2 hasta el final
print(peliculas[2:])


# Añadir elemento a la lista
cantantes.append("Dj Zatox") # append agregar al final
print(cantantes)

# Recorrer lista


nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
         peliculas.append(nueva_pelicula)

print("\n****Listado Peliculas****")

for pelicula in peliculas :
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")


# Lista multidimensionales: son listas que contienen otras listas en su interior.
# En este caso, cada sublista representa un contacto con [nombre, email].

print("\n**** Listado de contactos ****")

# Definimos la lista de contactos con sublistas.
contactos = [
    ['Luis', 'luis@gmail.com'],
    ['Felipe', 'felipe@gmail.com'],
    ['Elian', 'elian@gmail.com']
]

# Imprime toda la lista de contactos (la estructura completa).
print(contactos)
print("\n")

# Accede a un elemento específico: en este caso, el email del segundo contacto.
# contactos[1] -> segunda lista ['Felipe', 'felipe@gmail.com']
# contactos[1][1] -> segundo elemento de esa lista ('felipe@gmail.com')
print(contactos[1][1])
print("\n")

# Recorremos la lista de contactos con un bucle for anidado.
for contacto in contactos:  # Recorre cada sublista (cada contacto).
    for elemento in contacto:  # Recorre cada elemento dentro de la sublista (nombre o email).
        
        # Si el índice del elemento es 0, significa que es el nombre.
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:  # Si no, es el email.
            print("Email: " + elemento)
    
    # Salto de línea para separar visualmente cada contacto.
    print("\n")

