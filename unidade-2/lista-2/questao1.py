while True:
    try:
        primeiraNota = float(input("Qual é a nota da PRIMEIRA unidade? "))
        segundaNota = float(input("Qual é a nota da SEGUNDA unidade? "))
        terceiraNota = float(input("Qual é a nota da TERCEIRA unidade? "))

        nota = ((primeiraNota * 2) + (segundaNota * 3) + (terceiraNota * 4)) / 9
        
        if nota >= 7:
            print("Francisco está aprovado!")
        
        elif nota < 3:
            print("Francisco está reprovado!")

        else:
            print("Francisco está em prova final!")

        break

    except:
        print("Insira um valor válido!")