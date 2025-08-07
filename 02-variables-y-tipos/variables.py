"""
Una variable es un contenedor de información.
Sirve para guardar datos que luego puedes reutilizar o modificar.

Podemos crear muchas variables y cada una puede tener un tipo de dato distinto.
"""

# -------------------- CREAR VARIABLES ------------------------

# Guardamos texto (tipo string) en una variable
texto = "Hola Mundo desde Python" 

# Otro string, en una variable diferente
texto2 = "Luis"

# Guardamos un número entero (tipo int)
numero = 60

# Guardamos un número decimal (tipo float)
decimal = 6.7

# -------------------- MOSTRAR VALORES ------------------------

# Imprimimos el contenido de cada variable en la consola
print(texto)
print(texto2)
print(numero)
print(decimal)


# -------------------- CONCATENACIÓN DE STRINGS ------------------------

# Concatenar (unir) varias cadenas de texto para formar una sola
nombre = "Luis"
apellido = "Guzman"
pais = "Chile"

# Forma 1: usando `+` y agregando espacios manualmente
print(nombre + " " + apellido + " - " + pais)

# Forma 2: usando f-strings (recomendado, más limpio y moderno)
print(f"{nombre} {apellido} - {pais}")

# Forma 3: usando .format()
print("Hola me llamo {} {} y mi país es: {}".format(nombre, apellido, pais))


# -------------------- CONCATENAR TEXTO + NÚMERO ------------------------

# Si queremos unir texto y números, el número debe convertirse a texto (str)
texto3 = "Hola soy un texto"
numerito = str(779)  # Convertimos el número 779 a string

# Ahora sí podemos concatenar sin error
print(texto3 + " " + numerito)





