from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("program")
label = Label(root, text ="Hello World!")
root.geometry("200x100")
style = Style()
style.configure('btn', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')
btn = Button(root, text = "Destroy",style = 'btn', command= root.destroy)
root.mainloop()