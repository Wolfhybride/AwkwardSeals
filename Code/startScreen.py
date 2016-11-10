from main import *
from menuStartScreen import startMenu
from help import help

def startScreenfunction():
    def return_entry(data):                                   #gets input and returns it
        data = console.get()
        console.delete(0, END)
        console.insert(0, string = ">>> ")
        choose(data)
        return data

    console.bind('<Return>', return_entry)

    startMenu()
    write("\n")

    def choose(choice):                                         #raw data that write(string) prints to the screen as text
       mainWindow.delete(0, END)
       if (choice == ">>> 1"):
           startMenu()
           write("")
           write(">>> You choose: Continue!")

       elif (choice == ">>> 2"):
           startMenu()
           write("")
           write(">>> You choose: New Game!")

       elif (choice == ">>> 3"):
           startMenu()
           write("")
           write (">>> You choose: Load Game!")

       elif (choice == ">>> 4"):
           startMenu()
           write("")
           write(">>> You choose: Settings!")

       elif (choice == ">>> 5"):
            raise SystemExit

       elif (choice == ">>> help"):
           help()
           if choice == ">>> ":
               startMenu()
               write(">>> You choose: help!")
       else:
           startMenu()
           write("")
           if choice != ">>> ":
                write(">>> That is not a valid command!")
           else:
               write("")

startScreenfunction()

mainloop()