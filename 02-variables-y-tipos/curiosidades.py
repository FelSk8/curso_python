# Creamos una variable de texto con nuestro nombre
mi_texto = "luis"

# Creamos otra variable que contiene un texto con comillas dobles dentro
mi_texto2 = ' "felipe" '  # Usamos comillas simples afuera para poder usar comillas dobles adentro

# Concatenamos (unimos) las dos variables en una sola, separadas por un espacio
texto_unido = mi_texto + " " + mi_texto2

# Mostramos el texto unido por consola
print(texto_unido)


# Ahora unimos las dos variables pero usando \n para hacer un salto de línea
texto_unido = mi_texto + " \n " + mi_texto2  # \n crea un salto de línea entre los textos

# Mostramos el resultado con el salto de línea
print(texto_unido)
