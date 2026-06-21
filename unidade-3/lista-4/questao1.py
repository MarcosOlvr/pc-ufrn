def divisores(numero):
    lista_divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            lista_divisores.append(i)

    return lista_divisores


N = int(input("Qual o valor de N? "))

numeros = []

print("Digite os valores: ")
for i in range(N):
    num = int(input())
    numeros.append(num)

print("A classificação é:")

for num in numeros:
    divs = divisores(num)

    if len(divs) == 2:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo. Os divisores são: {divs}")