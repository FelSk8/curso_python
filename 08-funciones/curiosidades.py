# Definición de una función que recibe un parámetro (nombre)
def mi_funcion(nombre):
    # Retorna un saludo concatenando el texto con el nombre
    return "Hola que tal " + nombre


# Definición de una segunda función que recibe un parámetro (apellido)
def mi_segunda_funcion(apellido):
    # Retorna un saludo concatenando el texto con el apellido
    return "Hola que tal 2 " + apellido


# Variables que almacenan datos de entrada
nombre = " Luis"       # Observa que tiene un espacio inicial
apellido = "Guzman"

# Llamada a la primera función con el parámetro 'nombre'
print(mi_funcion(nombre))  
# → Imprime: Hola que tal  Luis

# Llamada a la segunda función con el parámetro 'apellido'
print(mi_segunda_funcion(apellido))  
# → Imprime: Hola que tal 2 Guzman
