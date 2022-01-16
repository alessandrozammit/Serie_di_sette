import random

a=0
ennevolte=int(input("quante volte: "))
for x in range (ennevolte):
    a=a+1
    b = [random.choice("R""N") for i in range(14)]
    #print (b)
    if (b[0:7]==b[7:14]):
        print (b[0:14])
        print ("trovato alla ",a,"serie ")
