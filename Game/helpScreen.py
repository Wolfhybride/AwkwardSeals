from main import *
from help import help

def startScreenderp():
    from startScreen import startScreenfunction

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

help()

def choose(choice):                                         #raw data that write(string) prints to the screen as text
   if (choice == ">>> "):
       startScreenderp()
       write("")

mainloop()