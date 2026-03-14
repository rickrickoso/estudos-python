#ANALISE DE FREQUENCIA

frase = input("Digite uma frase: ") #RECEBE A FRASE DO USUARIO
dic = {}                            #DICIONARIO VAZIO

for char in frase:                  #ITERA SOBRE CADA CARACTERE DA FRASE
    if char in dic:                 #VERIFICA SE ELE JÁ EXISTE
        dic[char] += 1              #SE SIM, ADICIONA +1 AO VALOR
    else:
        dic[char] = 1               #SE NAO, ADICIONA 1 AO VALOR
        
if " " in dic:                      #VERIFICA ESPAÇOS EM BRANCO E DELETA
    del dic[" "]

print(dic)                          #IMPRIME O DICIONARIO
