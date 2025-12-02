animales = ["Leon", "Tigre", "Gato"]

animales.insert(0, "Raton")
animales.append("Perro")

animales.pop()
del animales[3]

if "Tigre" in animales:
    print("Tigre esta en la lista")
