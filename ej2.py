a = []
num = 0

num = int(input("Dame un nuemro (-1 para salir): "))
while num != -1:
    a.append(num)
    num = int(input("Dame un nuemro (-1 para salir): "))

total = 0
for i in a:
    total += i

print(total)
