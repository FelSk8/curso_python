# Programación orientada a objetos (POO u OOP)

# Definir una clase (molde para crear más objetos de ese tipo)
class Coche:
    # Atributos por defecto (todos los coches comienzan con estos valores)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballos_fuerza = 500
    plazas = 2

    # ------------------- MÉTODOS -------------------

    # Métodos SET: sirven para CAMBIAR el valor de un atributo
    def setColor(self, color):
        self.color = color   # Cambia el atributo 'color'

    def setModelo(self, modelo):
        self.modelo = modelo  # Cambia el atributo 'modelo'

    # Métodos GET: sirven para OBTENER el valor de un atributo
    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo

    # Método para aumentar la velocidad en 1
    def acelerar(self):
        self.velocidad += 1

    # Método para disminuir la velocidad en 1
    def frenar(self):
        self.velocidad -= 1

    # Método para obtener la velocidad actual
    def getVelocidad(self):
        return self.velocidad

# ------------------- USO DE LA CLASE -------------------

# Crear un objeto (instanciar la clase)
coche = Coche()

print("Coche 1: ")

# Cambiamos atributos con métodos SET
coche.setColor("amarillo")
coche.setModelo("Murciélago")

# Mostramos información del coche con métodos GET
print(coche.marca, coche.getModelo(), coche.getColor())  
# -> Ferrari Murciélago amarillo

# Velocidad inicial
print("Velocidad actual: ", coche.velocidad)  # -> 300

# Usamos los métodos para modificar la velocidad
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

# Velocidad final
print("Velocidad actual: ", coche.velocidad)  # -> 303


print("-----------------------------------------------")

# Crear mas objetos

coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("Coche 2: ")
print(coche2.marca, coche2.getModelo(), coche2.getColor())  