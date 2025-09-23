"""
Ejercicio D: Detectar tipos de datos
"""

# 1. Variables
mi_lista = ["pera", "naranja", "melon", "sandia", "durazno"]   # lista
ciudad = "Santiago"                                            # string
numero = 33.5                                                  # decimal
verdadero = True                                               # booleano

# 2. Función que traduce tipos
def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == float:
        result = "NÚMERO DECIMAL"
    elif tipo == bool:
        result = "BOOLEANO"  
    return result

# 3. Función que comprueba el tipo
def comprobarTipado(dato, tipo):
    if isinstance(dato, tipo):
        return f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        return "El tipo de dato no es correcto"

# 4. Pruebas
print(comprobarTipado(mi_lista, list))
print(comprobarTipado(ciudad, str))
print(comprobarTipado(numero, float))
print(comprobarTipado(verdadero, bool))
