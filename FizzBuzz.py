# FizzBuzz

for i in range (1,51):                          #itera até 50
    if (i % 3 == 0) and (i % 5 == 0)== True:    #verifica se o numero é divisivel por 3 e por 5
        print ("FizzBuzz")
    elif i % 3 == 0:                            #verifica se o numero é divisivel por 3
        print ("Buzz")      
    elif i % 5 == 0:
        print("Fizz")                           #verifica se o numero é divisivel por 5
    else:
        print(i)

