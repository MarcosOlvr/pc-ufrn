maiorValor = 0
exit = True

print("Informe os gastos no dia: ")
while exit: 
    valor = float(input())

    if valor == 0:
        exit = False

    if valor > maiorValor:
        maiorValor = valor

if maiorValor == 0: 
    print("Você não teve gastos hoje!")
else:
    print(f"O seu maior gasto hoje foi R${maiorValor}")