"""
# BUCLE WHILE

El bucle WHILE es una estructura de control que **repite instrucciones** 
mientras se cumpla una condición lógica.

Estructura:

while condición:
    bloque de instrucciones
    actualización del contador (si no, entra en bucle infinito)
"""


# Inicializamos el contador en 1
contador = 1

# Mientras el contador sea menor o igual a 100, se ejecuta el bucle
while contador <= 100:
    # Mostramos el número actual
    print(f"Estoy en el número: {contador}")
    
    # Aumentamos el contador en 1 para evitar bucle infinito
    contador = contador + 1

    
print("-----------------------------------------")

# Reiniciamos el contador
contador = 1

# Creamos un string que inicialmente contiene "0"
muestrame = str(0)

# Mientras el contador sea menor o igual a 100
while contador <= 100:
    # Concatenamos el número actual al string, separado por coma
    muestrame = muestrame + " , " + str(contador)
    
    # Aumentamos el contador
    contador = contador + 1

# Mostramos el resultado final
print(muestrame)



print("\n############### EJEMPLO ##############")

# Pedimos al usuario un número
numero_usuario = int(input("¿De qué número quieres la tabla?: "))

# Validamos que el número sea al menos 1
if numero_usuario < 1:
    numero_usuario = 1

# Mostramos un encabezado con f-string
print(f"### Tabla del número {numero_usuario} ###")

# Inicializamos el contador para la tabla
contador = 1

# Repetimos mientras contador sea menor o igual a 10
while contador <= 10:
    # Mostramos el resultado de la multiplicación
    print(f"{numero_usuario} X {contador} = {numero_usuario * contador}")
    
    # Aumentamos el contador
    contador = contador + 1

# Este bloque else se ejecuta solo cuando termina el bucle normally (sin break)
else:
    print("TABLA TERMINADA")
