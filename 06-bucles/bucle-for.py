"""
# FOR
Estructura básica del bucle FOR en Python:

for variable in elemento_iterable (lista, rango, etc):
    BLOQUE DE INSTRUCCIONES

Significa: 
 “Por cada elemento dentro de una secuencia, repite este bloque de instrucciones”
"""

# Inicializamos dos variables: un contador y un resultado acumulador
contador = 0
resultado = 0

# Creamos un bucle for que va desde 0 hasta 4 (el 5 no se incluye)
for contador in range(0, 5):
    # Mostramos el valor actual del contador (lo convertimos a string para poder concatenar)
    print("Voy por el " + str(contador))

    # Acumulamos el valor del contador en la variable resultado
    # Esto es lo mismo que: resultado = resultado + contador
    resultado += contador

# Mostramos el resultado final acumulado fuera del bucle
print(f"El Resultado es: {resultado}")


# Imprime un título para separar los ejemplos
print("\n############### EJEMPLO ##############")

# Pedimos al usuario un número para mostrar su tabla de multiplicar
numero_usuario = int(input("¿De qué número quieres la tabla? :"))

# Validamos que el número no sea menor que 1
if numero_usuario < 1:
    numero_usuario = 1  # Si lo es, lo corregimos a 1

# Mostramos un encabezado personalizado con f-string
print(f"#### Tabla de Multiplicar del número {numero_usuario} ####")

# Creamos un bucle que recorre los números del 1 al 10
for numero_tabla in range(1, 11):
    """
    Este bloque está comentado, pero sirve como ejemplo de control:
    
    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos")
        break  # Saldría del bucle si se cumple esa condición
    """
    
    # Mostramos cada multiplicación en formato: 5 x 1 = 5
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario * numero_tabla}")

# Este else se ejecuta solo si el for termina correctamente (sin usar break)
else:
    print("Tabla Terminada")
