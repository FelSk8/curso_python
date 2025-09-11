"""
Ejercicio 1. Hacer un programa que tenga una lista 
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Crear función que recorra lista y devuelva string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# Crear la lista con 8 números enteros
numeros = [1, 2, 5, 15, 8, 10, 4, 7]


# Crear una función que recorra la lista y devuelva un string con sus elementos
def mostrarLista(lista):
    resultado = ""

    # Se va concatenando cada elemento de la lista en formato string
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado
   

# 1. Recorrer y mostrar la lista
print("***** RECORRER Y MOSTRAR *****")
"""
for numero in numeros:
    print(numero)   # Forma simple, pero aquí se reemplazó por la función
"""
print(mostrarLista(numeros))   # Llamada a la función que devuelve los números como texto


# 2. Ordenar y mostrar la lista
print("****** ORDENAR Y MOSTRAR ******")
numeros.sort()  # Ordena la lista 'numeros' de menor a mayor
print(mostrarLista(numeros))


# 3. Mostrar su longitud
print("****** MOSTRAR SU LONGITUD ******")
print(len(numeros))   # len() devuelve la cantidad de elementos en la lista


# 4. Búsqueda en la lista
print("****** BÚSQUEDA EN LA LISTA ******")

# Se pide al usuario un número para buscarlo
busqueda = int(input("Introduce el numero: "))

# Se valida que el dato ingresado sea un número entero positivo
comprobar = isinstance(busqueda, int)   # Comprueba que sea entero
while not comprobar or busqueda <= 0:   # Mientras no sea válido, vuelve a pedirlo
    busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducido el {busqueda}")


print(f"##### Buscar en la lista el numero {busqueda} #####")

# index() busca el número dentro de la lista y devuelve su posición (índice)
search = numeros.index(busqueda)  
print(f"El numero buscado existe en la lista, es el indice {search}")
