n = int(input("Qual o N? "))
if n > 0:
    print("Digite os valores:")
    valores = []

    for i in range(n):
        valores.append(int(input()))

    op = int(input("Qual a OP? "))
    a = int(input("Qual é o A? "))
    b = int(input("Qual é o B? "))
    if op == 0:
        valor = valores[a - 1] + valores[b - 1]
        print(f"{valores[a-1]} + {valores[b-1]} = {valor}")

    if op == 1:
        valor = valores[a - 1] * valores[b - 1]
        print(f"{valores[a-1]} * {valores[b-1]} = {valor}")

    else: 
        print("Operação deve ser 0 (soma) ou 1 (multiplicação)")

else:
    print("N deve ser um inteiro maior que 0")