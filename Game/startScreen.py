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

    derp = 0
    def next():
        global derp
        if derp > 16:
            return 0
        derp = derp + 1
        return derp

    startMenu()
    write("\n")

    def choose(choice):                                         #raw data that write(string) prints to the screen as text
       mainWindow.delete(0, END)
       if (choice == ">>> 1"):
           startMenu()
           write("")
           write(">>> You choose: Play!")
           hurr = 1
       if hurr == 1:
           write("\n")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
       elif (hurr == 1) and (choice == (">>> ")):
           next()
           # if (derp == 0):
           #
           if (derp == 1):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
               write("")
           elif (derp == 2):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
               write("")
           elif (derp == 3):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
           elif (derp == 4):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
               write("")
           elif (derp == 5):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
           elif (derp == 6):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
           elif (derp == 7):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.5'])
               write("")
           elif (derp == 8):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.6'])
               write("")
           elif (derp == 9):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.7'])
               write("")
           elif (derp == 10):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.8'])
               write("")
           elif (derp == 11):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
           elif (derp == 12):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("\n" * 26)
           elif (derp == 13):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("\n" * 24)
           elif (derp == 14):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.9'])
               write("\n" * 22)
           elif (derp == 15):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.9'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.10'])
               write("\n" * 20)
           elif (derp == 16):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.9'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.10'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.11'])
               write("\n" * 18)
           elif (derp == 17):
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.9'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.10'])
               write("")
               write(doc['root']['levels']['bart']['dialoog']['barttext1.11'])
               write("")
               write("Set sail for fail!")
               write("")
               write("    " + str(doc['root']['ascii']['boat']['boat_0']))
               write(" " + str(doc['root']['ascii']['boat']['boat_1']))
               write("   " + str(doc['root']['ascii']['boat']['boat_2']))
               write("\n" * 12)

       elif (choice == ">>> 2"):
           startMenu()
           write("")
           write(">>> You choose: New Game!")

       elif (choice == ">>> 3"):
           startMenu()
           write("")
           write(">>> You choose: Settings!")

       elif (choice == ">>> 4"):
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
       write("")
startScreenfunction()

mainloop()