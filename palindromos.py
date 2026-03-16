#DETECTOR DE PALINDROMO

print("DETECTOR DE PALINDROMO (PALAVRA IGUAL DE TRAZ PRA FRENTE)")

word = input("Digite a palavra: ") #RECEBE A PALAVRA

if word == word[::-1]:              #UTILIZANDO SLICING, TESTAMOS A STRING DE TRAZ PARA FRENTE (var[::-1] == rav) 
    print("É um palindromo!!")      #RESPOSTA POSITIVA
else:
    print ("Não é palindromo...")   #RESPOSTA NEGATIVA

    
    
