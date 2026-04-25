while True:
    try:
        valor = float(input("Qual é o valor da compra? "))
        metodoDePagamento = input("Como gostaria de pagar à vista (V) ou à prazo (P)? ")

        metodoDePagamento = metodoDePagamento.capitalize()

        if metodoDePagamento == "V":
            desconto = valor * (5/100) 
            print(f"Valor à pagar R${valor - desconto:.2f}")

        elif metodoDePagamento == "P":
            valorComJuros = valor * (1 + (8/100))
            parcela = valorComJuros / 3

            print(f"O valor à pagar é 3 parcelas de R${parcela:.2f}")

        else:
            raise Exception()

        break

    except:
        print("Digite um valor ou método de pagamento válido!")