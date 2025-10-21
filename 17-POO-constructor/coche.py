# Definir una clase (molde para crear más objetos de ese tipo)
class Coche:
    # Atributos por defecto (todos los coches comienzan con estos valores)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballos_fuerza = 500
    plazas = 2

    def __init__(self, color, marca, modelo, velocidad , caballos_fuerza, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballos_fuerza = caballos_fuerza
        self.plazas = plazas

    # ------------------- MÉTODOS -------------------

    # Métodos SET: sirven para CAMBIAR el valor de un atributo
    def setColor(self, color):
        self.color = color   # Cambia el atributo 'color'

    def setModelo(self, modelo):
        self.modelo = modelo  # Cambia el atributo 'modelo'

    def setMarca(self, marca):
        self.marca = marca

    # Métodos GET: sirven para OBTENER el valor de un atributo
    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo
    
    def getMarca(self):
        return self.marca

    # Método para aumentar la velocidad en 1
    def acelerar(self):
        self.velocidad += 1

    # Método para disminuir la velocidad en 1
    def frenar(self):
        self.velocidad -= 1

    # Método para obtener la velocidad actual
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):

        info = "---- Informacion del coche ----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info