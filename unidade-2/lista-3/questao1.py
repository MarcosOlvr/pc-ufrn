while True:
    try:
        alturaLevi = float(input("Altura inicial de Levi: "))
        crescimentoLevi = float(input("Taxa de crescimento de Levi: "))
        alturaHiago = float(input("Altura inicial de Hiago: "))
        crescimentoHiago = float(input("Taxa de crescimento de Hiago: "))

        if alturaLevi >= alturaHiago:
            print("Erro: Hiago deve ser maior que Levi inicialmente")
            break

        elif crescimentoHiago >= crescimentoLevi:
            print("Erro: A taxa de crescimento de Levi deve ser maior que a de Hiago.")
            break

        anos = 0

        while alturaLevi < alturaHiago:
            alturaLevi += (crescimentoLevi / 100)
            alturaHiago += (crescimentoHiago / 100)
            anos += 1

        print(f"Serão necessários {anos} anos para que Levi seja maior que Hiago.")
        
        break

    except:
        print("Insira um valor válido!")