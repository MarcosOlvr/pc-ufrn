numeros = input()
valores = numeros.split()

for i in range(len(valores)):
    valores[i] = int(valores[i])

dentro = False

if valores[4] >= valores[0] and valores[4] <= valores[2]:
    if valores[5] >= valores[1] and valores[5] <= valores[3]:
        dentro = True

if dentro:
    print("Dentro!")

else:
    print("Fora!")