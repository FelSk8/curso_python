nombre = "Luis Guzman"

# Saber el tipo de dato de la variable
print(type(nombre))   # <class 'str'>

# Detectar el tipado con isinstance()
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

# Negación con not: verificar que no es float
if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")


# ----------------------------
# Limpiar espacios con strip()
frase = "       mi contenido      "
print(frase)          # Con espacios
print(frase.strip())  # Sin espacios al inicio y final


# ----------------------------
# Eliminar variables con del
year = 2025
print(year)
del year
# print(year)  # → Esto daría error porque year ya no existe


# ----------------------------
# Comprobar si una variable está vacía
texto = " ff "

if len(texto) <= 0:  # len mide cuántos caracteres tiene
    print("La variable está vacia")
else:
    print("La variable tiene contenido: ", len(texto))


# ----------------------------
# Encontrar caracteres o palabras dentro de un string
frase = "La vida es bella"
print(frase.find("vida"))   # Devuelve la posición donde empieza "vida"


# ----------------------------
# Reemplazar palabras
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)   # → "La moto es bella"


# ----------------------------
# Transformar a mayúsculas y minúsculas
print(nombre)          # "Luis Guzman"
print(nombre.lower())  # "luis guzman"
print(nombre.upper())  # "LUIS GUZMAN"
