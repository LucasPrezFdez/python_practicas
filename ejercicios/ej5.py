array = []

with open("numeros.txt", "r", encoding="utf-8") as f:
    numeros = f.read()

array = numeros.split(";")

salida = []
for i in array:
    salida.append(int(i) ** 2)

print(salida)
