"""
Ejercicio 3
Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo)
de los 60 primeros numeros naturales 
resolverlo con for y while
"""
#while
contador = 0
while contador <= 60:
    # Mostramos el resultado de la multiplicación
    #print(f"{contador} * {contador} = {contador * contador}")
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    
    # Aumentamos el contador
    contador = contador + 1


#for

for contador in range(61):
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")