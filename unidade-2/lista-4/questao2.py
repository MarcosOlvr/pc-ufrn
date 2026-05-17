meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

numeroDoMes = int(input("Qual é o número do mês? "))

if numeroDoMes < 1 or numeroDoMes > 12:
    print(f"Erro: não existe mês de número {numeroDoMes}! Por favor, digite um número entre 1 e 12.")

else:
    print(f"O mês é {meses[numeroDoMes-1]}")