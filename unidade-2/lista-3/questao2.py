while True:
    try:
        valores = []

        for i in range(10):
            valor = float(input(f"Insira a taxa do exame do paciente {i + 1}: "))
            valores.append(valor)

        mediaAritmetica = 0
        for valor in valores:
            mediaAritmetica += valor

        mediaAritmetica = mediaAritmetica / 10

        mediaGeometrica = 1
        for valor in valores:
            mediaGeometrica *= valor

        mediaGeometrica = mediaGeometrica ** (1/10)

        mediaHarmonica = 0
        for valor in valores:
            mediaHarmonica += 1 / valor
        mediaHarmonica = 10 / mediaHarmonica

        erroHarmonica = (mediaHarmonica - mediaAritmetica) / mediaAritmetica
        erroGeometrica = (mediaGeometrica - mediaAritmetica) / mediaAritmetica
        erroMedio = (erroHarmonica + erroGeometrica) / 2 

        print("")

        print(f"Média aritmética: {mediaAritmetica:.2f}")
        print(f"Média harmônica: {mediaHarmonica:.2f}")
        print(f"Média geométrica: {mediaGeometrica:.2f}")
        print(f"Erro médio: {(erroMedio * 100):.2f}%")

        break
        
    except:
        print("Insira um valor válido!")