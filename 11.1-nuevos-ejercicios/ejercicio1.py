"""
Ejercicio A: Lista de nombres y búsqueda
"""

# 1. Crear una lista con al menos 7 nombres de personas
lista_nombres = ["luis", "isaac", "camela", "jack", "maria", "felipe", "ana"]

# 2. Crear función que recorra la lista y devuelva todos los nombres separados por guiones
def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + elemento
        resultado += "\n"
    return resultado

# 3. Mostrar la lista original
print("***** LISTA ORIGINAL *****")
print(mostrarLista(lista_nombres))

# 4. Ordenar la lista en orden alfabético inverso y mostrarla
lista_nombres.sort(reverse=True)
print("***** LISTA ORDENADA (inversa) *****")
print(mostrarLista(lista_nombres))

# 5. Pedir un nombre por teclado y comprobar si existe en la lista
busqueda = input("Introduce el nombre que quieres buscar en la lista: ")

# Validar que no sea vacío
while busqueda.strip() == "":
    busqueda = input("Introduce el nombre que quieres buscar en la lista: ")

print(f"Has introducido el nombre: {busqueda}")

# Buscar en la lista
if busqueda in lista_nombres:
    search = lista_nombres.index(busqueda)
    print(f"El nombre buscado existe en la lista, está en el índice {search}")
else:
    print("El nombre no existe en la lista")
