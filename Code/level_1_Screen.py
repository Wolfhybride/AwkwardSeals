from main import *
from test import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

derp = 0

def next():
    global derp
    derp = derp+ 1

def choose(choice):                                         #raw data that write(string) prints to the screen as text
   if choice == (">>> "):
       next()
       #write(str(derp))

       if (derp == 0):
           write(str(derp))

       elif (derp == 1):
            koffietext1()

       elif (derp == 2):
            lifttext1()

       elif (derp == 3):
        studenttext()

       else:
           global derp
           derp = 0
   #if (choice == ">>> "):
   #    print("")

mainloop()