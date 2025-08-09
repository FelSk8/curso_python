# Ejercicio 6: Mostrar las tablas de multiplicar del 1 al 10

# Bucle externo que va del 1 al 10, para cada tabla de multiplicar
for cabecera in range(1, 11):
    # Imprime el título de la tabla actual
    print(f"#### La tabla del número {cabecera} ####")

    # Bucle interno que recorre del 1 al 10 para hacer las multiplicaciones
    for numero in range(1, 11):
        # Imprime la multiplicación actual, por ejemplo: "3 x 4 = 12"
        print(f"{numero} x {cabecera} = {numero * cabecera}")

    # Imprime una línea en blanco para separar tablas y que se vea más ordenado
    print("\n")
