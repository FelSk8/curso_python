# Importamos el módulo 'open' desde io (aunque realmente bastaría con usar 'open' directamente de Python).
from io import open

# Importamos pathlib para trabajar con rutas de archivos de forma más segura.
import pathlib
#módulo que nos permite copiar, mover y borrar archivos
import shutil  

# Obtenemos la ruta absoluta de la carpeta donde estamos ejecutando el script.
# pathlib.Path().absolute() devuelve algo como: "C:/Users/Luis/Documents/proyecto"
# Luego concatenamos el nombre del archivo que queremos crear/abrir.
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

# Abrimos (o creamos si no existe) el archivo en modo '+a':
# - 'a' = append (agregar contenido al final del archivo).
# - '+' = permite también lectura, aunque aquí solo escribimos.
archivo = open(ruta, "+a")

# Escribimos una línea de texto dentro del archivo.
# El '\n' es un salto de línea, para que el texto no quede todo pegado.
archivo.write("****Soy un texto metido desde python****\n")

# Cerramos el archivo (muy importante para liberar memoria y asegurar que el texto se guarde).
archivo.close()

# Abrir archivo en modo lectura
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer TODO el contenido como un solo string
# contenido = archivo_lectura.read()
# print(contenido)

# Leer todas las líneas y guardarlas en una lista
# readline() = solo 1 línea
# readlines() = TODAS las líneas en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

# Recorremos cada línea de la lista
for frase in lista:
    # Podemos dividir la frase en palabras con split() si queremos procesarla
    # lista_frase = frase.split()
    # print(lista_frase)

    # Imprimimos cada línea con un guion al inicio
    print("- " + frase.strip())  # strip() elimina saltos de línea al final


# copiar
# Definir la ruta del archivo original
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

# Definir la ruta donde se copiará el archivo
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"

# Copiar el archivo (contenido completo)
shutil.copyfile(ruta_original, ruta_nueva)

print("Archivo copiado con éxito 🚀")

