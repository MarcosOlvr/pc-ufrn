temperatura = input()
valor, unidade = temperatura.split()
valor = float(valor)
valorC = 0
valorF = 0
valorK = 0

match unidade.lower():
    case "c":
        valorC = valor
        valorF = (valor * (9/5)) + 32
        valorK = valor + 273.15

    case "f":
        valorC = (valor - 32) * (5/9)
        valorF = valor
        valorK = (valor - 32) * (5/9) + 273.15

    case "k":
        valorC = valor - 273.15
        valorF = (valor - 273.15) * 9/5 + 32
        valorK = valor

    case _:    
        print("Coloque uma unidade  de temperatura válida!")

print(f"Temperatura em Celsius: {valorC:.2f} °C")
print(f"Temperatura em Fahrenheit: {valorF:.2f} °F")
print(f"Temperatura em Kelvin: {valorK:.2f} °K")