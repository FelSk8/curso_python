# Ejercicio 7: Mostrar todos los números impares entre dos números dados por el usuario

# Pedimos el primer número y convertimos a entero
numero1 = int(input("Ingresa el primer número: "))

# Pedimos el segundo número y convertimos a entero
numero2 = int(input("Ingresa el segundo número: "))

# Validamos que el primer número sea menor que el segundo
if numero1 < numero2:
    # Recorremos desde numero1 hasta numero2 inclusive
    for contador in range(numero1, numero2 + 1):
        # Si el número es impar (no divisible por 2)
        if contador % 2 != 0:
            # Lo mostramos en pantalla
            print(f"{contador} : es impar")
else:
    # Mensaje de error si el rango es incorrecto
    print("Error: El número 1 tiene que ser menor que el número 2")
