#SEQUENCIA DE FIBONACCI N+1 = (N-1) + (N-2)
a=0
b=1

n = int(input("Digite o número até onde vai: ")) #USUARIO ESCOLHE ATÉ ONDE VAI A SEQUENCIA
while b <= n:
    print (b)        
    a, b = b, a+b    #ATUALIZA OS VALORES, FAZENDO A CONTA A -> B / B -> A + B 
    
