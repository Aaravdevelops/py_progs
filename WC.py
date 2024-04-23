import os
print("Hello, this is python and I am going to count the number of lines present in your desired file name..........")
filen=input("Please Enter the file name<file extension should be included>:")
if os.path.isfile(filen):
    os.system("ls")
    os.system(f"wc -w '{filen}'.")
else:
    print("It's a CAP,File does not exist")