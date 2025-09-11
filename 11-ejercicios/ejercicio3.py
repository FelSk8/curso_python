"""
Ejercicio 3. Programa que compruebe si una variable está vacía y, 
si está vacía, rellenarla con texto en minúsculas
y luego mostrarla en mayúsculas.
"""

# Variable inicial con un espacio (simulando que puede estar vacía)
texto = " "

# Usamos strip() para quitar espacios a la izquierda y derecha
# Luego comprobamos si la longitud es 0 => significa que está vacía
if len(texto.strip()) <= 0:
    # Si la variable está vacía, le damos un texto en minúsculas
    texto = "hola soy un texto en minusculas"
    
    # Lo mostramos en MAYÚSCULAS usando upper()
    print(texto.upper())
else:
    # Si la variable NO está vacía, mostramos su contenido
    print(f"La variable tiene contenido: {texto}")
