class User:
    def __init__(self, nombre, array_de_textos):
        self.nombre = nombre
        self.array_de_textos = array_de_textos


fichero = open("mensajes.txt", "r")
