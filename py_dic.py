print("Hey!, yo this is a locker made by Aarav here you go!")
Harsh ={'Gender': 'Male', 'Eligible to vote': 'Yes', 'Devices':'Yes'}
Puja ={'Gender': 'Female', 'Eligible to vote': 'Yes', 'Devices':'Yes'}
Aarav ={'Gender': 'Male', 'Eligible to vote': 'No', 'Devices':'No'}
Jeeva ={'Gender': 'Female', 'Eligible to vote': 'No', 'Devices':'No'}
a = input("Who's data do you want?")
if (a=="Harsh"):
    print(Harsh, "This is all the data feeded to me for this name.")
elif (a=="Puja"):
    print(Puja, "This is all the data feeded to me for this name.")
elif (a=="Aarav"):
    print(Aarav, "This is all the data feeded to me for this name.")
elif (a=="Jeeva"):
    print(Jeeva, "This is all the data feeded to me for this name.")
elif (a=="ALL"):
    print("this is for Harsh", Harsh)
    print("this is for Jeeva", Jeeva)
    print("this is for Puja", Puja)
    print("this is for Aarav", Aarav)
else:
    print("can't find for the following one!")
print("this file may get updated soon, ", "thanks for executing this file!")
print("VERSION 1.O")