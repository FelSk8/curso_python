"""
Funciones:
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando la función tantas veces como sea necesario.

Sintaxis básica:
def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(valor_parametro)  # Ejemplo de invocación
"""

# ==== EJEMPLO 1 ====

print("#### EJEMPLO 1 ####")

# Definición de la función (no recibe parámetros)
def muestraNombre():
    # Instrucciones que se ejecutarán cuando se llame a la función
    print("Luis")
    print("Jorge")
    print("Pascal")
    print("\n")  # Salto de línea para separar salidas

# Invocación de la función
muestraNombre()

# Podemos llamarla todas las veces que queramos
muestraNombre()


# ==== EJEMPLO 2 ====

print("#### EJEMPLO 2 ####")

# Definimos la función que recibe dos parámetros: nombre y edad
def mostrarTuNombre(nombre, edad):
    # Mostramos el nombre
    print(f"Tu nombre es: {nombre}")

    # Evaluamos si la edad es mayor o igual a 18
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

# Solicitamos datos al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Llamamos a la función pasando los valores ingresados como argumentos
mostrarTuNombre(nombre, edad)


# ==== EJEMPLO 3 ====

print("#### EJEMPLO 3 ####")

# Definimos la función que muestra la tabla de multiplicar de un número
def tabla(numero):
    print("\n")  # Salto de línea para mejor presentación
    print(f"La tabla de multiplicar del número: {numero}")
   
    # Recorremos del 1 al 10 para multiplicar
    for contador in range(1, 11):
        operacion = numero * contador
        print(f"{numero} X {contador} = {operacion}")

    print("\n")  # Salto de línea para separar tablas

# Pedimos al usuario el número cuya tabla quiere ver
numero = int(input("Ingresa el número que quieres para la tabla de multiplicar: "))
# Llamamos a la función para mostrar su tabla
tabla(numero)


# ==== EJEMPLO 3.1 ====

print("#### EJEMPLO 3.1 ####")

# Usamos un bucle para mostrar todas las tablas del 1 al 10
for numero_tabla in range(1, 11):
    tabla(numero_tabla)  # Llamamos a la función para cada número
