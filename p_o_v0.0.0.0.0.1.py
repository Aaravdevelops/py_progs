import getpass
print("Hey! this is your Password Organizer")
a = input("Do you want to Organize the Password? ")
if (a=="y"):
    b = input("do you have a google account? ")
    if (b=="y"):
        c = input("type the google email address: ")
        cc = getpass.getpass("type the google account password")
        with open("passes.txt",'w') as file:
            file.write(c)
            file.write("\n")
            file.write(cc)
            file.write("___________________________________________________________________________________________________________________________________")
        print("the data was entered successfully!")
    elif (b =="n"):
        d = input("do you have a yaahoo account? ")
        if (d=="y"):
            e = input("enter the yaaho email address: ")
            ee = getpass.getpass("enter the yaahoo password")
            with open("passes.txt",'w') as file:
                file.write(e)
                file.write("\n")
                file.write(ee)
                file.write("_______________________________________________________________________________________________________________________________")
                print("the data was entered successfully")
                
        elif (d=="n"):
            f = input("do you have a microsoft account? ")
            if (f=="y"):
                g = input("enter the microsoft email address:")
                gg = getpass.getpass("enter the password")
                with open("passes.txt",'w') as file:
                    file.write(g)
                    file.write("\n")
                    file.write(gg)
                    file.write("___________________________________________________________________________________________________________________________")
                    print("the data was entered successfully")
                    
            elif (f=="n"):
                h = input("do you have a amazon account? ")
                if (h=="y"):
                    i =  input("enter the amazon account address: ")
                    ii = getpass.getpass("enter the amazon account password")
                    with open("passes.txt",'w') as file:
                        file.write(i)
                        file.write("\n")
                        file.write(ii)
                        file.write("_______________________________________________________________________________________________________________________")
                        print("the data was entered successfully")
                        
                else:
                    print("sorry, i did'nt get that.")
            else:
                print("sorry, i did'nt get that.")
        else:
            print("sorry, i did'nt get that.")
    else:
        print("sorry, i did'nt get that.")
else:
    print("sorry, i did'nt get that")
