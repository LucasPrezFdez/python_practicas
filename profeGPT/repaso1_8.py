alumnos = ["Ana", "Luis", "Carlos", "Marta"]
notas = (8, 9, 7, 10)

informacion = {}

for i, alumno in enumerate(alumnos):
    informacion[f"{alumno}"] = notas[i]

print(informacion)

aprovados = set()

for nombre, nota in informacion.items():
    if nota >= 8:
        aprovados.add(nombre)

alumnos.append("Lucia")
notas = notas + (6,)

informacion = {}
aprovados = set()

for i, alumno in enumerate(alumnos):
    informacion[f"{alumno}"] = notas[i]

for nombre, nota in informacion.items():
    if nota >= 8:
        aprovados.add(nombre)

print(informacion)
print(aprovados)
