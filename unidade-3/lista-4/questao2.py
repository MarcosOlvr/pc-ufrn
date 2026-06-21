def par(numero):
    if (numero % 2) == 0:
        return 0
    
    else:
        return 1

numeros = []   
soma = 0

for i in range(4):
    num = int(input(f"Digite número {i+1}: "))
    numeros.append(num)

for numero in numeros:
    if par(numero) == 0:
        soma += numero

print(f"Soma dos números pares: {soma}")