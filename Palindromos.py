# Palindrome Detector

print("DETECTOR DE PALINDROMO (PALAVRA IGUAL DE TRAZ PRA FRENTE)") #saudacao

word = input("Digite a palavra: ") #recebe o possivel palindromo

if word == word[::-1]:              #var[::-1] == rav [é o slicing da string] 
    print("É um palindromo!!")      #resposta positiva
else:
    print ("Não é palindromo...")   #resposta negativa

    
    
