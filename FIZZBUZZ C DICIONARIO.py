#FIZZBUZZ C/ DICIONARIO
d = {(True, True): "FizzBuzz", (True, False):"Fizz", (False, True):"Buzz"}
for i in range (1,51):   
    t = (i % 3 == 0, i % 5 == 0)
    r = d.get(t, i)
    print(r)
        
"""
dicionario = {"chave":"valor","chave1":"valor1"}
0
print(dicionario.get("chave")) 

"""
