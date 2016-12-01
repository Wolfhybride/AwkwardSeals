from main import *
from menuStartScreen import startMenu
from help import help
from save import save

nameOpen = open("name.txt", "r")
name = nameOpen.readlines()

healthOpen = open("health.txt", "r")
health = healthOpen.readlines()

energyOpen = open("energy.txt", "r")
energy = energyOpen.readlines()

moneyzOpen = open("moneyz.txt", "r")
moneyz = moneyzOpen.readlines()

inventoryOpen = open("inventory.txt", "r")
inventory = inventoryOpen.readlines()

map(str, name)
map(int, health)
map(int,energy)
map(int,moneyz)


def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

derp = -3
hurr = 0
level = 0

def next():
    global derp
    derp = derp + 1
    return derp

startMenu()
write("\n")


def choose(choice):                                         #raw data that write(string) writes to the screen as text

   if (choice == ">>> 1"):  # Start spel + Uitleg
       startMenu()
       write(">>> You choose: Play!\n")
       global hurr
       hurr = 1
#########################################################################################################################
   # Proloog Begin
#########################################################################################################################
   elif (hurr == 1):
       next()
       write("")
       if (choice == (">>> ") and (derp == -2)):
           write("This is a text based game where you use commands to execute commands to get further in the\n     story.\n")
           write("Commands include:\n")
           write("help - List of available commands")
           write("save - Save your progress in the game")
           write("ENTER key - Further the dialoge\n")
           write("First you will get the prologue, and after that your adventure will begin!\n")
           write("Press the ENTER key to begin!")
           write("\n" * 13)
       elif (choice == (">>> ") and (derp == -1)):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("\n"*23)
       elif (choice == (">>> ") and (derp == 0)):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("\n"*20)
       elif (choice == (">>> ")) and (derp == 1):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("\n"*18)
       elif (derp == 2):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("\n"*16)
       elif (derp == 3):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("")
           write(". . .")
           write("\n"*14)
       elif (derp == 4):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("")
           write(". . .")
           write("")
           write("* Klas wordt rumoerig *")
           write("\n"*12)
       elif (derp == 5):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("")
           write(". . .")
           write("")
           write("* Klas wordt rumoerig *")
           write("")
           write(". . .")
           write("\n"*10)
       elif (derp == 6):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("")
           write(". . .")
           write("")
           write("* Klas wordt rumoerig *")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("\n"*8)
       elif (derp == 7):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("")
           write(". . .")
           write("")
           write("* Klas wordt rumoerig *")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write("* Je leest braaf je textboek en maakt de vragen van hoofdstuk 1. *")
           write("\n"*6)
       elif (derp == 8):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("")
           write(". . .")
           write("")
           write("* Klas wordt rumoerig *")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write("* Je leest braaf je textboek en maakt de vragen van hoofdstuk 1. *")
           write("")
           write("Docent Bart: Oke, jullie hoeven alle opdrachten pas aan het einde van de periode in te \n     leveren. Maar de final assignments moeten vanaf nu elke week worden nagekeken in de les.")
           write("\n"*3)
       elif (derp == 9):
           write("Om de cursus programmeren succesvol af te ronden voor je ICT studie moet je alle opdrachten\n     inleveren. De docent die je hierbij begeleid is Bart. Het is de eerste dag op de studie.")
           write("")
           write("Docent Bart: Welkom allemaal bij de cursus Python. Ik wil graag dat we hoofdstuk 1 binnen \n     een uur hebben afgerond.")
           write("")
           write("Student1: Meneer hoe werkt python?")
           write("")
           write("Docent Bart: Mag ik helaas niet vertellen, dat moet je zelf uitzoeken.")
           write("")
           write(". . .")
           write("")
           write("* Klas wordt rumoerig *")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write("* Je leest braaf je textboek en maakt de vragen van hoofdstuk 1. *")
           write("")
           write("Docent Bart: Oke, jullie hoeven alle opdrachten pas aan het einde van de periode in te \n     leveren. Maar de final assignments moeten vanaf nu elke week worden nagekeken in de les.")
           write("")
           write("Docent Bart: Ik wil dus aan het einde van de periode jullie portfolio hebben in mijn e-mail \n     met alle opdrachten en final assignments.")
           write("")
       elif (derp == 10):
           write("Student 1: Dat wordt simpel, toch?")
           write("\n"*24)
       elif (derp == 11):
           write("Student 1: Dat wordt simpel, toch?")
           write("")
           write(". . .")
           write("\n"*22)
       elif (derp == 12):
           write("Student 1: Dat wordt simpel, toch?")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("\n"*20)
       elif (derp == 13):
           write("Student 1: Dat wordt simpel, toch?")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("\n"*18)
       elif (derp == 14):
           write("Student 1: Dat wordt simpel, toch?")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("\n" * 16)
       elif (derp == 15):
           write("Student 1: Dat wordt simpel, toch?")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write("* Zo veel dagen later dat je nog maar 5 dagen hebt om alles te maken en nog niks hebt *")
           write("\n" * 14)
       elif (derp == 16):
           write("Student 1: Dat wordt simpel, toch?")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write(". . .")
           write("")
           write("* Zo veel dagen later dat je nog maar 5 dagen hebt om alles te maken en nog niks hebt *")
           write("")
           write(". . .")
           write("\n"*12)
       elif (derp == 17):
           write("""
                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░░░░
                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███▀█░░░░
                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░██░░░
                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░██░░░
                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄██░░░░██░░
                              ░░░░░░░░░░░░░░░░▄▄█▀▀▀▀█▄▄▄▄███▄░░░██░░
                              ░░░░░░░░░░░░░▄█▀░░░░░░░░░▀▀▀▀█░▀█░░██░░
                              ░░░░░░░░░░░░█▀░░░░░░░░░░░░░░░▀█▄█▀▀▀░░░
                              ░░░░░░░░░░░▄▀░░░░░░░░░░░░░░░░▀█▄░░░░░░░
                              ░░░░░░░░░░░▀█▄░█░░▄▀░░░░░░░▄▄█░░░░░░░░░
                              ░░░░░░░░▄▄▄▄█▀▀▀██▄▄░░░░░░▄▀░░░░░░░░░░░
                              ░░░░▄▄██▄▀▀░░░░░█▀░░░░░░▄██▄░░░░░░░░░░░
                              ░░▄██▀▀░░░░░░░░▄█░░░░░▄█▀▄█░▀▀█▄▄▄▄▄▄▄▄
                              ░██▀░░░░░░░░▄██░░░░░░▄▀▄▄▀░░░░░░░░░░░░░
                              █▀▀░░░░░░▄█▀▄░▀▄▄▄▄██▀▀▀░░░░░█░░░░░░░░░
                              █░░░░░▄▄▀░░░░█░░░░░░░░░░░░░░░▀░░░░░░░░░
                              ░▀▀▀▀▀▀░░░░░░░█░░░░░░░░░░░░░░░▀▀█▀▀▀▀▀▀
                              ░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░█▀░░░░░░
                              ░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░▄█░░░░░░░
           """)
           write("")
           write("                     Well, I haven't been very productive now, have I?")
           write("\n" * 1)
       elif (derp == 18):
           write("- Objectief: Verzamel alle opdrachten, anders wordt je uitgeschreven uit de opleiding!")
           write("")
           write("Set sail for fail!")
           write("")
           write("    __/\__")
           write(" ~~~\____/~~~~~~")
           write("   ~  ~~~   ~")
           write("\n" * 18)
       elif (derp == 19):
           global level
           level = 1
#########################################################################################################################
# Proloog Eind
#########################################################################################################################

#########################################################################################################################
# Level 1 Begin
#########################################################################################################################
       if (level == 1):
           write(doc['root']['levels']['verdieping1']['dialoog']['text1.0'])
           write("\n" * 24)
           if (level == 1) and (choice == ">>> inspect"):                           #INSPECT
               write(doc['root']['levels']['verdieping1']['dialoog']['text1.0'])
               write("")
               write(">>> inspect")
               write("")
               write("- " + doc['root']['levels']['verdieping1']['dialoog']['text1.1'])
               write("- " + doc['root']['levels']['verdieping1']['dialoog']['text1.2'])
               write("\n"*19)
           elif (level == 1) and (choice == ">>> interact koffiezet apparaat"):     #INSPECT koffiezet apparaat
               write(doc['root']['levels']['verdieping1']['dialoog']['text1.0'])
               write("")
               write(">>> interact koffiezet apparaat")
               write("")
               write("- " + doc['root']['levels']['verdieping1']['dialoog']['koffietext1.1'])
               write("")
               write("- " + doc['root']['levels']['verdieping1']['dialoog']['koffietext1.2'])
               write("- Je energy is nu: ")
               write("\n"*17)
           elif (level == 1) and (choice == ">>> stats"):               #STATS
               write(doc['root']['levels']['verdieping1']['dialoog']['text1.0'])
               write("")
               write(">>> stats")
               write("")
               write("Name: " + str(*name))
               write("Health: " + str(*health))
               write("Energy: " + str(*energy))
               write("Moneyz: "+ str(moneyz))
               write("Inventory: ")
               for line in inventory:
                    write("- " + str(line))
               write("\n"*8)
           elif (level == 1) and (choice == ">>> save"):
               save()
               write("You saved the game!")
               write("\n"*24)
           elif (level == 1) and (choice == ">>> interact student"):
               import battleScreen
           elif (level == 1) and (choice == ">>> help"):                #HELP
               write("")
               write("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

               write("             " + str(doc['root']['ascii']['studentLife']['studentLife_0']))
               write("            " + str(doc['root']['ascii']['studentLife']['studentLife_1']))
               write("           " + str(doc['root']['ascii']['studentLife']['studentLife_2']))
               write("            " + str(doc['root']['ascii']['studentLife']['studentLife_3']))
               write("            " + str(doc['root']['ascii']['studentLife']['studentLife_4']))
               write("           " + str(doc['root']['ascii']['studentLife']['studentLife_5']))

               write("")
               write("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
               write("")
               write("")
               write("Available commands:")
               write("inspect - inspect the environment")
               write("interact (object name) - interact with an object in the room")
               write("stats - display your stats")
               write("inventory - display your inventory")
               write("save - save the game.")
               write("exit - exit the game")
               write("")
               write("Press ENTER to return to the main menu.")
               write("\n\n\n\n\n\n")

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