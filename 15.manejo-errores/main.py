# Capturar excepciones y manejar errores en el código
# Este código es susceptible a fallos/errores (por ejemplo, si no se escribe nada en el input)
"""
try:
    # Pedimos al usuario su nombre
    nombre = input("¿Cuál es tu nombre?: ")

    # Si el nombre tiene más de 1 carácter, se guarda correctamente
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    # Imprimimos la variable (Si no se cumple el if, puede dar error porque nombre_usuario no se crea)
    print(nombre_usuario)

# Si ocurre un error en el bloque try, se ejecuta este bloque
except:
    print("Ha ocurrido un error, mete bien el nombre")

# Si no ocurre ningún error en el try, se ejecuta este bloque
else:
    print("Todo ha funcionado correctamente")

# Este bloque SIEMPRE se ejecuta, haya o no error
finally:
    print("Fin de la iteración!!")


# Crear la lista con 8 números enteros
numeros = [1, 2, 5, 15, 8, 10, 4, 7]

try:
    print("****** BÚSQUEDA EN LA LISTA ******")

    # Se pide al usuario un número para buscarlo
    busqueda = int(input("Introduce el número: "))

    # Se valida que el dato ingresado sea un número entero positivo
    comprobar = isinstance(busqueda, int)   # Comprueba si es un entero
    while not comprobar or busqueda <= 0:   # Mientras no sea válido, vuelve a pedirlo
        busqueda = int(input("Introduce el número: "))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"##### Buscar en la lista el número {busqueda} #####")

    # index() busca el número dentro de la lista y devuelve su posición (índice)
    search = numeros.index(busqueda)  
    print(f"El número buscado existe en la lista, está en el índice {search}")

# Si ocurre un error (por ejemplo, número no está en la lista), se ejecuta este bloque
except:
    print("El número no está en la lista, lo siento!!")

"""
"""

# Múltiples excepciones
try:
    # Se pide un número al usuario
    numero = int(input("Número para elevarlo al cuadrado: "))

    # Se calcula el cuadrado y se muestra
    print("El cuadrado es: " + str(numero * numero))

# Si ocurre un error de tipo (TypeError)
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código!!")

# Si ocurre un error de valor (ej: ingresar letras en vez de números)
# except ValueError:
#     print("Introduce un número correcto !!")

# Captura cualquier otra excepción (la más genérica)
except Exception as e:
    print("Ha ocurrido un error:", type(e).__name__)
"""

# Excepciones personalizadas o lanzar excepción
try:
    # Pedir nombre y edad
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    # Validaciones personalizadas
    if edad < 5 or edad > 110:   # Edad fuera de rango lógico
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:       # Nombre demasiado corto
        raise ValueError("El nombre no está completo")
    else:
        # Si todo está bien
        print(f"Bienvenido {nombre}")

# Captura de ValueError
except ValueError:
    print("Introduce los datos correctamente!!")

# Captura genérica de cualquier otro error inesperado
except Exception as e:
    print("Existe un error:", e)
