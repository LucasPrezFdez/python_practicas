notas = [4, 6, 10, 6, 8, 9]

pesos = (0.4, 0.3, 0.1, 0.2, 0.5, 0.2)


promedio = 0
for i in range(len(notas)):
    promedio += notas[i] * pesos[i]


notasSlice = notas[-3:]
print(min(notasSlice))
print(max(notasSlice))

notas.append(5)
print(notas)
