valor = int(input())
if(valor == 0):
    print("Insira um valor entre 1 e 99")

for i in range(valor):
    print(f"{i + 1:3d}", end="")
    for j in range(1, valor):
        print(f"{(abs(i - j) + 1):4d}", end="")
    print("")
print("")