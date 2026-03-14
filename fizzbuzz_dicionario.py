#FIZZBUZZ C/ DICIONARIO
d = {(True, True): "FizzBuzz", (True, False):"Fizz", (False, True):"Buzz"}         #DICIONARIO DE RESULTADOS
for i in range (1,51):                                                             #ITERA DE 1 ATÉ 50
    t = (i % 3 == 0, i % 5 == 0)                                                   #TUPLA DE BUSCA DE RESULTADOS
    r = d.get(t, i)                                                                #BUSCA A TUPLA DENTRO DO DICIONÁRIO, OU O CONTADOR DA ITERAÇÃO QUANDO NÃO ENCONTRAR
    print(r)
        
"""
dicionario = {"chave":"valor","chave1":"valor1"}
print(dicionario.get("chave")) 

"""
