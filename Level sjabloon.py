from main import *
from Levelsjabloon import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

forwardText = 0

#forward text is de (enter) tussen de texten zodat de text in stukken word verdeeld.
def next():
    global forwardText
    forwardText = forwardText + 1

def choose(choice):                                         #raw data that write(string) prints to the screen as text
   if choice == (">>> "):
       next()
       #write(str(derp))

       if (forwardText == 0):
           write(str(forwardText))

       elif (forwardText == 1):
            koffietext()

       elif (forwardText == 2):
            lifttext()

       elif (forwardText == 3):
        studenttext()

       else:
           global forwardText
           forwardText = 0
   #if (choice == ">>> "):
   #    print("")

mainloop()
