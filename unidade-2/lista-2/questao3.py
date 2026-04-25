while True:
    try:
        pessoas = int(input("Qual o número de pessoas? "))

        idades = []

        for x in range(pessoas):
            idade = int(input(f"Informe a idade pessoa {x + 1}: "))
            idades.append(idade)

        soma = 0
        for i in idades:
            soma += i

        print(f"A média de idade das pessoas é {soma / pessoas:.0f} anos")

        break

    except:
        print("Informe um valor válido!")