n = int(input("Quantidade de jogadores: "))
if n > 0:
    saque = 0
    bloqueio = 0
    ataque = 0 
    saqueCorreto = 0
    bloqueioCorreto = 0
    ataqueCorreto = 0
    nome = ""
    print("Digite os dados de cada jogador: ")
    for i in range(n):
        nome, s, b, a, sCorreto, bCorreto, aCorreto = input().split()
        saque += int(s)
        ataque += int(a)
        bloqueio += int(b)
        saqueCorreto += int(sCorreto)
        bloqueioCorreto += int(bCorreto)
        ataqueCorreto += int(aCorreto)

    print(f"Pontos de Saque: {(saqueCorreto/saque)*100:.2f}%")
    print(f"Pontos de Bloqueio: {(bloqueioCorreto/bloqueio)*100:.2f}%")
    print(f"Pontos de Ataque: {(ataqueCorreto/ataque)*100:.2f}%")