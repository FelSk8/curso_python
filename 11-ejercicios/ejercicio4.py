"""
Ejercicio 4.
Crear un script que tenga 4 variables,
una lista, un string, un entero y un booleano
y que imprima un mensaje segun el tipo de dato de cada variable. 
Usar funciones
"""

# Esta función recibe un tipo de dato (list, str, int, bool)
# y lo traduce a un texto entendible.
def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        # OJO: aquí tenías un error con "=="
        # debe ser "=" para asignar el texto
        result = "BOOLEANO"  

    return result


# Esta función comprueba si un dato es del tipo indicado
def comprobarTipado(dato, tipo):
    # isinstance(dato, tipo) devuelve True si coincide
    test = isinstance(dato, tipo)
    result = ""

    if test:
        # Llamamos a traducirTipo, pero hay que pasar el tipo, no el dato
        result = f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"

    return result


# Creamos nuestras 4 variables
mi_lista = ["Hola mundo", 77]   # una lista
titulo = "Luis Guzman"          # un string
numero = 100                    # un entero
verdadero = True                # un booleano


# Comprobamos cada variable con su respectivo tipo
print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))
