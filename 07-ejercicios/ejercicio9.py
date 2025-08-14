# Ejercicio 9: Pedir números indefinidamente hasta que el usuario escriba 111

# Creamos un bucle infinito que solo se detendrá con "break"
while True:
    # Pedimos un número al usuario y lo convertimos a entero
    numero = int(input("Introduce un número (escribe 111 para salir): "))

    # Si el número es 111, salimos del bucle
    if numero == 111:
        print("Programa finalizado. Has escrito 111.")
        break
    else:
        # Si no es 111, mostramos el número que el usuario introdujo
        print(f"Has introducido el número {numero}")
