while True:
    try:
        numero = int(input("Digite um número inteiro: "))

        if numero == 0:
            raise Exception()

        listaDeNumeros = []
        resultado = 1

        for i in range(numero):
            listaDeNumeros.append(i + 1)

        for x in listaDeNumeros:
            resultado *= x

        print(f"Resultado do fatorial: {resultado}")

        break

    except:
        print("Digite um número válido (número precisa ser diferente de 0)!")