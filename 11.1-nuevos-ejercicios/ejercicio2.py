"""
Ejercicio B: Lista de cuadrados de números
"""

# 1. Crear lista vacía
Lista_vacia = []

# 2. Usar un for para guardar en la lista los cuadrados de los números del 1 al 20
#    range(1, 21) → genera números del 1 al 20 (el 21 no se incluye).
for contador in range(1, 21):  
    # Guardamos el cuadrado en la lista
    Lista_vacia.append(f"elemento - {contador ** 2}")  

    # contador empieza en 1 y llega hasta 20 → coincide con el índice (0 → 19)
    # Por eso NO da error, porque el índice nunca se pasa del rango.
    print("Mostrar con for: " + Lista_vacia[contador - 1])

print("----- Lista después del for -----")
print(Lista_vacia)


# 3. Usar un while para añadir a la lista los números del 21 al 30 al cuadrado
contador = 21

while contador <= 30:
    Lista_vacia.append(f"elemento - {contador ** 2}")  
    
    # OJO: aquí el índice de la lista ya no coincide con "contador".
    # Porque la lista tiene más elementos que solo "contador" posiciones.
    # Solución: usamos -1 para acceder SIEMPRE al último elemento agregado.
    print("Mostrar con while: " + Lista_vacia[-1])  

    contador = contador + 1


# 4. Mostrar toda la lista al final
print("----- Lista final -----")
print(Lista_vacia)
