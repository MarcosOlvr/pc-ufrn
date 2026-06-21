n = int(input("Quantos nomes? "))
if n > 0:
    nomes = []
    for i in range(n):
        nomes.append(input())

    print("Você digitou: ")
    for nome in nomes[::-1]:
        print(nome)