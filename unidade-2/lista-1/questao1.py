while True:
    try:
        distancia = float(input("Qual é a distância da viagem de ida e volta em quilômetros? "))
        kmPorLitro = float(input("Quantos quilômetros o carro percorre com cada litro de combustível? "))
        precoCombustivel = float(input("Qual é o preço em reais por litro de combustível? "))

        valor = (distancia / kmPorLitro) * precoCombustivel

        print(f"O valor em reais para realizar a viagem pretendida é: {valor:.2f}")

        break

    except:
        print("Insira um número válido")