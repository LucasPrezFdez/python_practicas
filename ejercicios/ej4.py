array = []

while True:
    name = input("Dame nombre: ")
    if name == "":
        break
    array.append(name)

if array:
    with open("nombres.txt", "w", encoding="utf-8") as f:
        for n in array:
            f.write(n + "\n")
