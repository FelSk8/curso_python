
def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

def calculadora(numero1, numero2, basicas=False):
    # Operaciones matemáticas
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    # Variable donde vamos a ir guardando los resultados como texto
    cadena = ""

    # Si "basicas" es True, mostramos solo suma y resta
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        # Si "basicas" es False (por defecto), mostramos multi y división
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)
        
    return cadena  # Devolvemos la cadena con los resultados