while True:
    try:
        valores = []

        for i in range(4):
            largura = float(input(f"Qual é a largura do lote {i + 1}? "))
            comprimento = float(input(f"Qual é o comprimento do lote {i + 1}? "))
            area = largura * comprimento
            valores.append(area)

        valor = 0
        for x in valores:
            valor += x

        print(f"A área total do terreno é {valor:.2f} m2")
        
        break
    
    except: 
        print("Insira um número válido")
