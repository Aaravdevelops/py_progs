print("Here I am!")
a = input("Did you call me?")
filen = "goals.txt"
if (a == "yes"):
    print("Here you go, I am a to do list creator")
    b = input("please enter your desired goal here: ")
    c = input("another one: ")
    d = input("another one: ")
    e = input("do you want to put some more?")
    if (e == "yes"):
        f = input("another one: ")
        g = input("another one: ")
        h = print("you have reached the maximum limit, now this data will be put in a file named: goals.txt")
        print(h)
        with open(filen,'w') as file:
            file.write("*  ")
            file.write(b)
            file.write("\n")
            file.write("*  ")
            file.write(c)
            file.write("\n")
            file.write("*  ")
            file.write(d)
            file.write("\n")
            file.write("*  ")
            file.write(f)
            file.write("\n")
            file.write("*  ")
            file.write(g)
            file.write("\n")
            print("the file was created in the pwd Successfully!")
    else:
        print("you've reached the maximum limit, now this data will be put in the file named: goals.txt")
        with open(filen,'w') as file:
            file.write("*  ")
            file.write(b)
            file.write("\n")
            file.write("*  ")
            file.write(c)
            file.write("\n")
            file.write("*  ")
            file.write(d)
            file.write("\n")
            print("the file was created inside the pwd Successfully")
else:
    print("Ok then, this file is closing!")
    print("file was clossed successfully")
