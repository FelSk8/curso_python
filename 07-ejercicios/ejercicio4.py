"""
Ejercicio 4
Pedir dos números al usuario y hacer todas las operaciones básicas de una calculadora
(mostrar los resultados en pantalla)
"""

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Evitar división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "Error: no se puede dividir por cero."

print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} y {numero2} es: {division if isinstance(division, str) else round(division, 2)}")
