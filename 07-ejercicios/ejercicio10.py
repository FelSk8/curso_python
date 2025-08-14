# Ejercicio 10:
# Pedir la nota de varios alumnos y mostrar cuántos aprobaron y cuántos reprobaron.

# Contador para recorrer a todos los alumnos
contador = 1

# Contadores para aprobados y reprobados
aprobados = 0
reprobados = 0

# Preguntamos cuántos alumnos hay
numero_alumnos = int(input("¿Cuántos alumnos tienes?: "))

# Bucle que pide la nota de cada alumno
while contador <= numero_alumnos:
    # Pedimos la nota del alumno actual
    nota = int(input(f"¿Qué nota quieres ponerle al alumno {contador}? "))

    # Si la nota es mayor o igual a 4, el alumno aprueba
    if nota >= 4:
        aprobados += 1
    else:
        reprobados += 1

    # Pasamos al siguiente alumno
    contador += 1

# Mostramos los resultados finales
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
