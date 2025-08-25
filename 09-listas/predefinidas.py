# Lista de cantantes
cantates = ["Dj Cooner", "Dj Isaac", "Dj Zatox", "Dj Malice"]

# Lista de números
numeros = [1, 2, 5, 15, 8, 10]

# -----------------------------
# ORDENAR LISTA
# El método sort() ordena los elementos de una lista de menor a mayor (en números) o alfabéticamente (en strings)
print(numeros)
numeros.sort()  # Ordena la lista 'numeros'
print(numeros)

# -----------------------------
# AÑADIR ELEMENTOS
# append() añade un elemento al final de la lista
cantates.append("Alicia")

# insert(posición, elemento) añade un elemento en una posición específica
cantates.insert(1, "Dalmata")
print(cantates)

# -----------------------------
# ELIMINAR ELEMENTOS
# pop(indice) elimina el elemento en la posición indicada (si no pones índice, borra el último)
cantates.pop(1)

# remove(valor) elimina el primer elemento que coincida con el valor indicado
cantates.remove('Dj Isaac')
print(cantates)

# -----------------------------
# DAR LA VUELTA A LA LISTA
# reverse() invierte el orden actual de los elementos en la lista
print(numeros)
numeros.reverse()
print(numeros)

# -----------------------------
# BUSCAR ELEMENTOS EN LA LISTA
# El operador "in" devuelve True si el elemento está en la lista, False si no
print('Dj Cooner' in cantates)

# -----------------------------
# CONTAR ELEMENTOS EN LA LISTA
# len(lista) devuelve el número total de elementos
print(len(cantates))

# -----------------------------
# CONTAR CUÁNTAS VECES APARECE UN ELEMENTO
# count(valor) devuelve cuántas veces aparece el valor indicado
print(numeros.count(1))

# -----------------------------
# CONSEGUIR EL ÍNDICE DE UN ELEMENTO
# index(valor) devuelve la posición (índice) del primer elemento que coincide con el valor
print(cantates.index("Dj Zatox"))

# -----------------------------
# UNIR DOS LISTAS
# extend(otra_lista) agrega todos los elementos de la segunda lista al final de la primera
cantates.extend(numeros)
print(cantates)
