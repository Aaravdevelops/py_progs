import os

print("Hello, this is Python and I am going to count the number of lines present in your desired file name...")

filen = input("Please Enter the file name <file extension should be included>: ")

try:
    if os.path.isfile(filen):
        os.system(f"wc -l '{filen}'")
    else:
        print("File does not exist.")
except Exception as e:
    print("An error occurred:", e)