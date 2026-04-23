while True:
    try:
        valorDaMulta = float(input("Qual é o valor original cobrado por cada multa? "))
        juros = float(input("Qual é a porcentagem de juros cobrada pelo Detran? "))
        qtyAmigos = float(input("Quantos amigos irão contribuir com as despesas? "))

        valorASerPago = ((valorDaMulta * 2) * (1 + juros / 100)) / qtyAmigos

        print(f"O valor em reais que cada amigo deverá pagar ao Detran é {valorASerPago:.2f}")

        break

    except:
        print("Insira um número válido")