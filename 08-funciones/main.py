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


# ==== EJEMPLO 4 ====
print("#### EJEMPLO 4 ####")

# Función con parámetros opcionales
def getEmpleado(nombre, dni = False):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    # Si el parámetro dni se pasa, se muestra
    if dni != False:
        print(f"DNI: {dni}")

# Llamamos a la función pasando nombre y dni
getEmpleado("Luis Guzman", 445484585)

# También podemos llamarla solo con el nombre (sin DNI)
getEmpleado("Jorge Pascal")




# ==== EJEMPLO 5 ====
# Parámetros + return (devolver datos)

print("#### EJEMPLO 5 ####")

# Función que recibe un nombre y devuelve un saludo en forma de texto
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo  # Devolvemos el saludo en lugar de imprimirlo directamente

# Al usar print(), mostramos el valor que la función devuelve
print(saludame("Luis Guzman"))



# ==== EJEMPLO 6 ====
# Función tipo calculadora con parámetros opcionales

print("#### EJEMPLO 6 ####")

def calculadora(numero1, numero2, basicas=False):
    # Operaciones matemáticas
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    # Variable donde vamos a ir guardando los resultados como texto
    cadena = ""

    # Si "basicas" es True, mostramos solo suma y resta
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        # Si "basicas" es False (por defecto), mostramos multi y división
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)
        
    return cadena  # Devolvemos la cadena con los resultados

# Llamamos a la función y mostramos los resultados
print(calculadora(5, 5, True))   # Suma y Resta
print(calculadora(5, 5))        # Multiplicación y División


# ==== EJEMPLO 7 ====
print("#### EJEMPLO 7 ####")

# Función que devuelve un texto con el nombre
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

# Función que devuelve un texto con el apellido
def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

# Función que llama a las dos funciones anteriores y devuelve todo junto
def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

# Llamada a la función principal y mostrar el resultado
print(devuelveTodo("Luis", "Guzman"))



# ==== EJEMPLO 8: Funciones lambda
print("\n#### EJEMPLO 8 ####")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2050))