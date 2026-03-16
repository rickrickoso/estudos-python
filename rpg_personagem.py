#FICHA DE RPG POR CÓDIGO

print("BEM VINDO A SAISCON\nMONTE SUA FICHA")

nome = input("Digite o nome do personagem: ")
especie = input("Digite sua espécie: ")
atributoF = int(input("Digite sua força(0-5): "))
atributoA = int(input("Digite sua agilidade(0-5): "))
atributoI = int(input("Digite sua intelecto(0-5): "))
print("\nSEU INVENTÁRIO ESTÁ VAZIO! ESCOLHA DOIS ITENS\n")
inventario = [input("Digite o primeiro item: "), input("Digite o segundo item: ")]        #RECEBE OS DADOS DO PERSONAGEM

personagem = {                                                                            #DICIONÁRIO DE PERSONAGEM
    "nome": nome,
    "especie": especie,
    "atributos": {                                                                        #SUBDICIONÁRIO DE ATRIBUTOS
        "forca": atributoF,
        "agilidade": atributoA,
        "intelecto": atributoI
        },
    "inventario": inventario
    }

for chave, valor in personagem.items():                                                    #ITERA NOS ITENS DO DICIONÁRIO
    if isinstance(valor,dict):                                                             #UTILIZA O isinstance DO PYTHON PARA VERIFICAR SE É UM SUBDICIONÁRIO.
        print(f"{chave.title()}")
        for sub_chave, sub_valor in valor.items():                                         #ITERA NOS ITENS DO SUBDICIONÁRIO
            print(f" -> {sub_chave.title()}:{sub_valor}")
    else:
        print(f"{chave.title()}:{valor}")                                                  #IMPRIME 
    


