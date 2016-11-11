from main import *
from menuStartScreen import startMenu
from help import help


def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

derp = -1
hurr = 0
level = 0
def next():
    global derp
    derp = derp + 1
    return derp

startMenu()
write("\n")


def choose(choice):                                         #raw data that write(string) prints to the screen as text
   mainWindow.delete(0, END)

   if (choice == ">>> 1"):  # Start spel + Uitleg
       startMenu()
       write("")
       write(">>> You choose: Play!\n")
       write("This is a text based game where you use commands to execute commands to get further in the\n     story.\n")
       write("Commands include:\n")
       write("help - List of available commands")
       write("save - Save your progress in the game")
       write("ENTER key - Further the dialoge\n")
       write("First you will get the prologue, and after that your adventure will begin!\n")
       write("Press the ENTER key to begin!")
       write("\n"*11)
       global hurr
       hurr = 1
#########################################################################################################################
   # Proloog Begin
#########################################################################################################################
   if (hurr == 1):
       next()
       write("")
       if (choice == '>>> 1'):
           print("OK!")
       if (choice == (">>> ") and (derp == 0)):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write("\n"*22)
       elif (choice == (">>> ")) and (derp == 1):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("\n"*21)
       elif (derp == 2):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("\n"*19)
       elif (derp == 3):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("\n"*17)
       elif (derp == 4):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("\n"*15)
       elif (derp == 5):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("\n" * 13)
       elif (derp == 6):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("\n" * 11)
       elif (derp == 7):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.5'])
           write("")
           write("\n" * 8)
       elif (derp == 8):
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.5'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.6'])
           write("\n" * 6)
       elif (derp == 9):
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.5'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.6'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.7'])
           write("\n" * 3)
       elif (derp == 10):
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.5'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.6'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.7'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.8'])
           write("\n"*1)
       elif (derp == 11):
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.2'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.3'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.4'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.5'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.6'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.7'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.8'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])

       elif (derp == 12):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("\n" * 25)
       elif (derp == 13):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("\n" * 23)
       elif (derp == 14):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.9'])
           write("\n" * 21)
       elif (derp == 15):
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.0'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.9'])
           write("")
           write(doc['root']['levels']['bart']['dialoog']['barttext1.10'])
           write("\n" * 19)
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
           write("\n" * 17)
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
           write("\n" * 11)
           hurr = 0
           global level
           level = 1
#########################################################################################################################
# Proloog Eind
#########################################################################################################################

#########################################################################################################################
# Level 1 Begin
#########################################################################################################################
   elif (level == 1):
       write(doc['root']['levels']['verdieping1']['dialoog']['text1.0'])
       write(doc['root']['levels']['verdieping1']['dialoog']['text1.1'])
       write("\n" * 23)

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

mainloop()