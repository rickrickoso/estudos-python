a=0
b=1

n = int(input("Digite o número até onde vai: "))
while b <= n:
    print (b)        
    a, b = b, a+b    # atualiza os valores
    
