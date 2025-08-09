# Ejercicio 5: Mostrar todos los números entre dos números dados por el usuario

# Solicita al usuario que ingrese el primer número y lo convierte a entero
numero1 = int(input("Ingresa el primer número: "))

# Solicita al usuario que ingrese el segundo número y lo convierte a entero
numero2 = int(input("Ingresa el segundo número: "))

# Verifica que el primer número sea menor que el segundo para continuar
if numero1 < numero2:
    # Recorre e imprime todos los números desde numero1 hasta numero2 inclusive
    for contador in range(numero1, numero2 + 1):
        print(contador)
else:
    # Muestra un mensaje de error si el primer número no es menor que el segundo
    print("El número 1 tiene que ser menor que el número 2")
