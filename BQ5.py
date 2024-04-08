print("Yo, this is a well coded project talking to you and i will calculate the perimetre and area of some shapes")
A=input("Which of the given shape you want to take out the perimetre or the area, S for Square, R for rectangle and C for Circle:")
if (A=="C"):
    D= input("Ci for circumference and Ar for Area:")
    E= int(input("The radius of the Circle in cms:"))
    if (D=="Ci"):
        Circumference= 2*3.14*E
        print("The circumference is:",Circumference)
    elif (D=="Ar"):
        Ar = 3.14*E*E
        print("The Area is:", Ar)
    else:
        print("sorry, Didn't find any thing like that. :~<")
elif(A=="S"):
    L= int(input("Enter the length of the square:"))
    F=input("Ae for Area and Peri for perimetre")
    if (F=="Ae"):
        Ae= L*L
        print("The area is:",Ae)
    elif (F=="Peri"):
        peri=4*L
        print("The perimetre is:",peri)
    else:
        print("Sorry, didn't find any thing like that")
elif (A=="R"):
    DD= input("Aa for Area and Pe for perimetre:")
    l=int(input("Please enter the length:"))
    b=int(input("Please enter the breadth:"))
    if (DD=="Aa"): 
        Aa= l*b
        print("the area is:",Aa)
    elif (DD=="Pe"):
        Pe= 2*l+b
        print("the perimetre is:",Pe)
    else:
        print("Oops,didn't sound anything like that")
else:
    print("Oops,didn't sound anything like that")