while True:
        try:        
            valor = 0
            pedido = 0

            while True:
                pedido = int(input("Digite o código do item: "))
                if pedido == -1:
                     break

                quantidade = int(input("Digite a quantidade: "))                
                
                if pedido == 100:
                    valor += 5.50 * quantidade

                elif pedido == 101:
                     valor += 15 * quantidade

                elif pedido == 103:
                     valor += 20 * quantidade

                elif pedido == 104:
                     valor += 18 * quantidade

                elif pedido == 105:
                     valor += 6 * quantidade

                else:
                     raise Exception()

            print(f"Total a pagar: R${valor:.2f}")

            break

        except:
             print("Insira um valor válido!")

