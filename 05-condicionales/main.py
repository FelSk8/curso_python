"""
# Condicional IF

Si se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI No:
    Se ejecutan otro grupo de instrucciones

Sintaxis básica:
if condicion:
    instrucciones
else:
    otras instrucciones

# Operadores de comparación
== igual
!= diferente
<  menor que
>  mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos
and Y
or  O
!   negacion
not NO

"""

# Ejemplo 1
print("############# EJEMPLO 1 #############")

color = "rojo"  # Variable que guarda el color favorito

# También podrías pedirlo por teclado así:
# color = input("Adivina cual es mi color favorito :")

# Usamos una condición para comparar si el color ingresado es "rojo"
if color == "rojo":
    # Si la condición se cumple, se ejecuta este bloque
    print("Bien mi color favorito es ROJO")
else:
    # Si no se cumple, se ejecuta este otro bloque
    print("Color incorrecto!!")


# Ejemplo 2
print("\n############# EJEMPLO 2 #############")

year = 2020  # Año actual (puedes cambiarlo o pedirlo con input)

# year = int(input("¿En qué año estamos? :"))

# Evaluamos si el año es mayor o igual a 2021
if year >= 2021:
    print("Estamos del 2021 en adelante")
else:
    print("Es un año anterior a 2021")


# Ejemplo 3
print("\n############# EJEMPLO 3 #############")

# Datos personales
nombre = "Luis Guzman"
ciudad = "Santiago"
continente = "America Latina"
edad = 33
mayoria_edad = 18  # Edad mínima para ser considerado mayor de edad

# Evaluamos si la edad es mayor o igual a la mayoría de edad
if edad >= mayoria_edad:
    # Si es mayor, mostramos mensaje de confirmación
    print(f"{nombre} Si eres mayor de edad!!")

    # Dentro del mismo bloque, evaluamos si vive fuera de América Latina
    if continente != "America Latina":
        print("El usuario No es de America Latina")
    else:
        print(f"Es de America Latina y de {ciudad}")
else:
    # Si no es mayor de edad
    print(f"{nombre} No es mayor de edad")


# Ejemplo 4
print("\n############# EJEMPLO 4 #############")

# Pedimos al usuario un número del 1 al 7 (días de la semana)
dia = 2  # También podrías probar con un número fijo
#dia = int(input("¿Ingresa el número de la semana? :"))

# Evaluamos qué día corresponde al número ingresado
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miércoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    # Si el número no es del 1 al 5, se considera fin de semana
    print("Es fin de semana")



# Ejemplo 5
print("\n############# EJEMPLO 5 #############")

# Definimos la edad mínima y máxima para trabajar
edad_minima = 18
edad_maxima = 65

# Se puede usar un valor fijo para pruebas:
edad_oficial = 18

# Pedimos al usuario que ingrese su edad y la convertimos a entero
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))

# Evaluamos si la edad está dentro del rango permitido para trabajar
# Usamos el operador lógico 'and' para comprobar ambas condiciones al mismo tiempo
if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    # Si ambas condiciones se cumplen, mostramos este mensaje
    print("¡Estás en edad de trabajar!")
else:
    # Si no cumple alguna de las dos condiciones, se ejecuta esto
    print("¡No estás en edad de trabajar!")



# Ejemplo 6
print("\n############# EJEMPLO 6 #############")

# Guardamos el nombre del país en una variable
pais = "mexico"

# Comprobamos si el país es uno de los que habla español
# Utilizamos el operador lógico OR (o), basta con que una condición sea verdadera
if pais == "mexico" or pais == "españa" or pais == "colombia":
    print(f"{pais} es un país de habla hispana !!")
else:
    print(f"{pais} no es un país de habla hispana :")



# Ejemplo 7
print("\n############# EJEMPLO 7 #############")

pais = "mexico"

# Aquí usamos NOT para negar toda la condición entre paréntesis
# Es decir, si el país NO es ninguno de los tres, se ejecuta el primer bloque
if not (pais == "mexico" or pais == "españa" or pais == "colombia"):
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SÍ es un país de habla hispana :)")


# Ejemplo 8
print("\n############# EJEMPLO 8 #############")

pais = "colombia"

# Aquí usamos AND para verificar que el país NO sea ninguno de los tres al mismo tiempo
# Solo se ejecuta el primer bloque si NO es ni mexico, ni españa, ni colombia
if pais != "mexico" and pais != "españa" and pais != "colombia":
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SÍ es un país de habla hispana :)")
