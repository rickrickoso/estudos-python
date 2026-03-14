#FIZZBUZZ

for i in range (1,51):                          #ITERA ATÉ 50
    if (i % 3 == 0) and (i % 5 == 0)== True:    #VERIFICA SE O NUMERO E DIVISIVEL POR 3 E POR 5 AO MESMO TEMPO
        print ("FizzBuzz")
    elif i % 3 == 0:                            #VERIFICA SE O NUMERO E DIVISIVEL POR 3
        print ("Buzz")      
    elif i % 5 == 0:
        print("Fizz")                           #VERIFICA SE O NUMERO E DIVISIVEL POR 5
    else:
        print(i)

