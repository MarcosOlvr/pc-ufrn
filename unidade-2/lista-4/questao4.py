pontuacao = 0
print("Informe as pontuações dos atletas. Digite -1 para encerrar")
listaDePontuacoes = []
while True:
    pontuacao = int(input())
    if pontuacao == -1:
        break

    listaDePontuacoes.append(pontuacao)

maiorPontuacao = 0
for x in listaDePontuacoes:
    if maiorPontuacao < x:
        maiorPontuacao = x

print(f"O recorde de pontos é {maiorPontuacao}")
