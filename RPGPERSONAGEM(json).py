#FICHA DE RPG POR CÓDIGO
import json

print("BEM VINDO A SAISCON\nMONTE SUA FICHA")

#COLETA DE DADOS
nome = input("Digite o nome do personagem: ")
especie = input("Digite sua espécie: ")
atributoF = int(input("Digite sua força(0-5): "))
atributoA = int(input("Digite sua agilidade(0-5): "))
atributoI = int(input("Digite sua intelecto(0-5): "))
print("\nSEU INVENTÁRIO ESTÁ VAZIO! ESCOLHA DOIS ITENS\n")
inventario = [input("Digite o primeiro item: "), input("Digite o segundo item: ")]

#CRIACAO DO DICIONARIO DO PERSONAGEM
personagem = {
    "nome": nome,
    "especie": especie,
    "atributos": {                      #SUB_DICIONARIO(DICIONARIO DE DICIONARIO)
        "forca": atributoF,
        "agilidade": atributoA,
        "intelecto": atributoI
        },
    "inventario": inventario
    }

print(json.dumps(personagem, indent=4, ensure_ascii=False))
