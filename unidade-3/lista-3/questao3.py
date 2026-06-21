n = int(input("Quantidade de alunos: "))
if n > 0:
    alunos = []
    print("Digite os nomes dos alunos: ")
    for i in range(n):
        alunos.append(input())

    novaLista = alunos[::-1]

    if n % 2 == 0:
        for i in range(n):
            if (i+1) % 2 == 0:
                alunos[i] = novaLista[i-1]
    
    else:
        for i in range(n):
            if (i+1) % 2 == 0:
                alunos[i] = novaLista[i]

    print("Nova lista:")
    for aluno in alunos:
        print(aluno)