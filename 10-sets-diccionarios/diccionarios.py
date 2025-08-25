"""
Un **Diccionario** en Python es un tipo de dato que almacena pares **clave : valor**.
Es similar a un objeto en JSON o un array asociativo en otros lenguajes.
Permite acceder a los valores mediante su clave.
"""

# Definición de un diccionario llamado persona
persona = {
    "nombre": "Luis",      # Clave 'nombre' con valor 'Luis'
    "apellido": "Guzman",  # Clave 'apellido' con valor 'Guzman'
    "pais": "Chile"        # Clave 'pais' con valor 'Chile'
}

# Acceder a un valor del diccionario usando la clave
print(persona["apellido"])  # Output: Guzman

# Mostrar solo las claves
print(persona.keys())  
# Resultado: dict_keys(['nombre', 'apellido', 'pais'])

# Mostrar solo los valores
print(persona.values())  
# Resultado: dict_values(['Luis', 'Guzman', 'Chile'])

# Mostrar pares (clave, valor)
print(persona.items())  
# Resultado: dict_items([('nombre', 'Luis'), ('apellido', 'Guzman'), ('pais', 'Chile')])


"""
Lista con diccionarios:
- Es una combinación de listas y diccionarios.
- Cada elemento de la lista es un diccionario que contiene información de un contacto.
- Permite almacenar varios registros con claves iguales (ej. 'nombre', 'email').
"""

# Definición de la lista de contactos
contactos = [
    {
        'nombre': 'Luis',
        'email': 'luis@gmail.com'
    },
    {
        'nombre': 'Felipe',
        'email': 'felipe@gmail.com'
    },
    {
        'nombre': 'Claudio',
        'email': 'claudio@gmail.com'
    }
]

# Acceder a un valor específico:
# contactos[0] -> primer diccionario
# ['nombre'] -> acceder al valor de la clave 'nombre' dentro del diccionario
print(contactos[0]['nombre'])  # Output: Luis

print("\nListado de contactos: ")

# Recorremos la lista de contactos
for contacto in contactos:
    # contacto es un diccionario dentro de la lista
    
    # Imprimimos el nombre usando la clave 'nombre'
    print(f"El nombre del contacto: {contacto['nombre']}")
    
    # Imprimimos el email usando la clave 'email'
    print(f"El email del contacto: {contacto['email']}")
    
    # Salto de línea para separar cada contacto
    print("\n")
