from main import *
from level_1 import level_1


def return_entry(data):  # gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string=">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

def save():
    nameOpen = open("name.txt", "w")
    nameOpen.write(str(name))
    nameOpen.close()

    HealthOpen = open("health.txt", "w")
    HealthOpen.write(str(health))
    HealthOpen.close()

    energyOpen = open("energy.txt", "w")
    energyOpen.write(str(energy))
    energyOpen.close()

    moneyzOpen = open("moneyz.txt", "w")
    moneyzOpen.write(str(moneyz))
    moneyzOpen.close()

    inventoryOpen = open("inventory.txt", "w")
    for line in inventory:
        inventoryOpen.write(str(line) + "\n")
    inventoryOpen.close()

derp = 0


def next():
    global derp
    if derp > 16:
        return 0
    derp = derp + 1
    return derp


name = "Mango"
health = 10
energy = 25
moneyz = 5
inventory = []



def choose(choice):  # raw data that write(string) writes to the screen as text
    write("\n")
    write(doc['root']['levels']['bart']['dialoog']['barttext1.1'])
    write("")
    if choice == (">>> "):
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

mainloop()
