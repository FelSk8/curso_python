"""
Variables locales: Se define dentro de la función y no se pueden usar fuera de ella,
solo están disponibles dentro. A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función 
y estan disponibles dentro y fuera de ellas.

"""

#Variables globales
frase = "Hola mi Nombre es Luis Felipe y soy de Chile"

print(frase)

def holaMundo():
    frase = "Hola Mundo"
    print("Dentro de la función: ")
    print(frase)

holaMundo()