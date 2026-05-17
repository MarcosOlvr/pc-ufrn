convidados = ["Daniel", "Aluizio", "Isabel", "Teles", "Eduardo"]
nome = input("Qual nome você quer verificar? ").strip()
estaNaLista = False

print("A lista contém os seguintes nomes:")
for convidado in convidados:
    print(convidado)
    if convidado.lower() == nome.lower():
        estaNaLista = True

if estaNaLista:
    print(f"O nome {nome} está na lista, acesso permitido!")

else:
    print(f"O nome {nome} não está na lista, acesso negado!")