import random

liste=[]
print("Type 'start' to start\nType 'cancel' to cancel")
while True:
    try:
        giris = input("Person who join giveaway: ")
        if giris == "cancel":
            sor = input("Person or Giveaway? (P/G)\n ")
            if sor == 'p' or sor == 'P':
                sor1 = input("Who?\n ")
                if sor1 in liste:
                    yer = liste.index(sor1)
                    liste.pop(yer)
                    print("Done..")
                else:
                    print("This person not in giveaway.")
            elif sor == 'g' or sor == 'G':
                try:
                    while True:
                        liste.pop()
                except:
                    print("Giveaway canceled")
        elif giris == "start":
            sor2 = int(input("How many person will win?\n "))
            sonuc = random.sample(liste,sor2)
            
            if len(liste) < sor2:
                print("Winner count can't be more than participants!")
                print("Please try again!")

            else:
                print("Winners: ",sonuc)
            
        else: 
            liste.append(giris)
            

    except:
        print("Wrong Input!\n")
