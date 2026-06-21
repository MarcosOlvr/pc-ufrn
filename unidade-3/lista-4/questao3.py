def imprimir(numero):
    for i in range(numero):
        for j in range(i+1):
            print(i+1, end=" ")
        print()

num = int(input("Digite o valor de n: "))
if num > 0:
    imprimir(num)

else:
    print("Valor inválido! Insira um número positivo maior que 0.")