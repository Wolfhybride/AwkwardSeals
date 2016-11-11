name = "Mango"
health = 15
energy = 25
moneyz = 5
inventory = ["Laptop", "Note_1", "Huiswerk opdracht 2.2", moneyz]
screen = ""

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

    return("")
