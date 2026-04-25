while True:
    try:
        peso = float(input("Informe seu peso (kg): "))
        altura = float(input("Informe sua altura (m): "))

        imc = peso / (altura * altura)

        if imc < 18.5:
            print("Abaixo do peso")

        elif imc >= 18.5 and imc < 25:
            print("Peso normal")

        elif imc >= 25 and imc < 30:
            print("Sobrepeso")

        elif imc >= 30:
            print("Obesidade")

        break
    
    except:
        print("Insira um valor válido!")