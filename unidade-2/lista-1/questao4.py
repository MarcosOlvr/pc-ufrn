while True:
    try:
        numero = int(input("Qual é o número inteiro que deve ser utilizado para gerar a sequência? "))

        valores = [numero-2, numero-1, numero+1, numero+2]

        soma = numero
        for x in valores:
            soma += x

        print(f"A sequência é a seguinte: {valores[0]} {valores[1]} {numero} {valores[2]} {valores[3]} {soma}")
        
        break
    
    except:
        print("Insira um número válido (inteiro)")

