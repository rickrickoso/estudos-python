#FICHA DE RPG POR CÓDIGO

print("BEM VINDO A SAISCON\nMONTE SUA FICHA")

nome = input("Digite o nome do personagem: ")
especie = input("Digite sua espécie: ")
atributoF = int(input("Digite sua força(0-5): "))
atributoA = int(input("Digite sua agilidade(0-5): "))
atributoI = int(input("Digite sua intelecto(0-5): "))
print("\nSEU INVENTÁRIO ESTÁ VAZIO! ESCOLHA DOIS ITENS\n")
inventario = [input("Digite o primeiro item: "), input("Digite o segundo item: ")]

personagem = {
    "nome": nome,
    "especie": especie,
    "atributos": {
        "forca": atributoF,
        "agilidade": atributoA,
        "intelecto": atributoI
        },
    "inventario": inventario
    }

for chave, valor in personagem.items():
    if isinstance(valor,dict):
        print(f"{chave.title()}")
        for sub_chave, sub_valor in valor.items():
            print(f" -> {sub_chave.title()}:{sub_valor}")
    else:
        print(f"{chave.title()}:{valor}")
    


