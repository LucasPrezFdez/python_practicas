class User:
    def __init__(self, nombre, array_de_textos):
        self.nombre = nombre
        self.array_de_textos = array_de_textos


users = {}

with open("mensajes.txt", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea:
            continue
        if "=" not in linea:
            continue
        nombre, texto = linea.split("=", 1)
        nombre = nombre.strip()
        texto = texto.strip()
        if nombre == "":
            continue
        if nombre not in users:
            users[nombre] = User(nombre, [])
        users[nombre].array_de_textos.append(texto)

for nombre, user in users.items():
    print(nombre, user.array_de_textos)
