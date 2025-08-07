# Tipo None: representa "nada", sin valor asignado (como null en otros lenguajes)
nada = None

# Tipo string (cadena de texto)
cadena = "Hola Soy Luis Guzman" 

# Tipo entero (número sin decimales)
entero = 99

# Tipo flotante (número con decimales)
flotante = 4.2

# Tipo booleano: solo puede ser True (verdadero) o False (falso)
booleano = True  # también puedes usar False

# Tipo lista (array en otros lenguajes), puede contener varios valores
lista = [10, 20, 30, 100]

# Lista con distintos tipos de datos (números y strings mezclados)
listaString = [10, "Hola", 20, "luis"]

# Tupla: como una lista, pero NO se puede modificar (es inmutable)
tuplaNoCambia = ("Luis", "Guzman")

# Diccionario: almacena datos con claves y valores (como un objeto en JavaScript o un JSON)
diccionario = {
    "nombre": "luis",
    "apellido": "guzman",
    "pais": "chile"
}


# ----------- IMPRIMIR VALORES -------------
# Mostramos el contenido de cada variable
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)


# ----------- MOSTRAR TIPO DE DATO -------------
# La función type() nos dice qué tipo de dato es cada variable
print(type(nada))          # NoneType
print(type(cadena))        # str
print(type(entero))        # int
print(type(flotante))      # float
print(type(booleano))      # bool
print(type(lista))         # list
print(type(listaString))   # list
print(type(tuplaNoCambia)) # tuple
print(type(diccionario))   # dict
