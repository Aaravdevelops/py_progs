print("this is using update function for dictionaries!")
Batch1 = {1:"Shubham", 2:"Sahil", 3:"Samarth", 4:"Ashok", 5:"Abdul"}
Batch2 = {1:"Akshit", 2:"Rachit", 3:"Rajvansh"}
pr = input("which batch's data do you want? or you want to update a batch?")
if (pr=="update"):
    a = input("which batch do you want to update?")
    if (a=="1"):
        Batch1.update(Batch2)
    elif (a=="2"):
        Batch2.update(Batch1)
    else:
        print("Sorry!, no command found like that.")
elif (pr=="Batch1"):
    print(Batch1, "This is all the data feeded to me for this name.")
elif (pr=="Batch2"):
    print(Batch2, "This is all the data feeded to me for this name.")
else:
    print("Sorry!, no command found like that.")
print("this file may get updated soon, ", "thanks for executing this file!")
print("VERSION 1.O")