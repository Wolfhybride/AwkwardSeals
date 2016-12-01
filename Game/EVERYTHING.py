from main2 import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

write("\n")

commandInput = []
commandOutput = []

prologue = []
level_1_dialogue = []

for line in doc["root"]["command"]["input"]:                        #commandInput
    commandInput.append(doc["root"]["command"]["input"][line])
for line in doc["root"]["command"]["output"]:                       #commandOutput
    commandOutput.append(doc["root"]["command"]["output"][line])

for line in doc["root"]["prologue"]:                                #prologue
    prologue.append(doc["root"]["prologue"][line])
for line in doc["root"]["level_1"]["dialogue"]:                     #level_1
    level_1_dialogue.append(doc["root"]["level_1"]["dialogue"][line])

screen = (doc["root"]["start"]["screen"] + ("\n"))

x = -1
y = 13

def next():
    global x
    x += 1
    global y
    y -= 2
    return x, y

write(screen + ("\n"*5))

def choose(data):                                         #raw data that write(string) writes to the screen as text
    if NameError:
        return None
    if data == ">>> ":                          # Blank
        write(doc["root"]["start"]["screen"])
        write("\n" * 5)
    elif (data in commandInput[0]):             # Start
        write(screen)
        write(str(commandOutput[0]))
        write("\n"*2)

        global level
        level = 0
    elif (data in commandInput[1]):             # Settings
        write(screen)
        write(str(commandOutput[1]))
        write("\n" * 2)
    elif (data in commandInput[2]):             # Stop
        write(screen)
        write(str(commandOutput[2]))
        write("\n" * 2)
    elif (data in commandInput[3]):             # help
        write(str(commandOutput[3]))
        write("\n"*7)
    elif (data in commandInput[4]):             # save
        write(screen)
        write(str(commandOutput[4]))
        write("\n" * 2)
    else:
        write(screen)
        write("This is not a valid command!")
        write("\n" * 2)

    if (data == ">>> ") and (level == 0):     # proloog
        next()
        print(x)
        try:
            if x == 0:
                y = 13
                write(prologue[0])
                write("\n" * int(y))
            elif (x == 1):
                global y
                y = 24
                write(prologue[x])
                write("\n" * y)
            elif (x == 2):
                y = y - 1
                write(prologue[x - 1])
                write("")
                write(prologue[x])
                write("\n" * y)
            elif (x == 3):
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 4):
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 5):
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 6):
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 7):
                write(prologue[x - 6] + "\n")
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 8):
                write(prologue[x - 7] + "\n")
                write(prologue[x - 6] + "\n")
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 9):
                write(prologue[x - 8] + "\n")
                write(prologue[x - 7] + "\n")
                write(prologue[x - 6] + "\n")
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 10):
                y = y - 1
                write(prologue[x - 9] + "\n")
                write(prologue[x - 8] + "\n")
                write(prologue[x - 7] + "\n")
                write(prologue[x - 6] + "\n")
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 11):
                y = y - 1
                write(prologue[x - 10] + "\n")
                write(prologue[x - 9] + "\n")
                write(prologue[x - 8] + "\n")
                write(prologue[x - 7] + "\n")
                write(prologue[x - 6] + "\n")
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 12):
                y = 25
                write(prologue[x])
                write("\n" * y)
            elif (x == 13):
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 14):
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 15):
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 16):
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 17):
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 18):
                y = y - 6
                write(prologue[x - 6] + "\n")
                write(prologue[x - 5] + "\n")
                write(prologue[x - 4] + "\n")
                write(prologue[x - 3] + "\n")
                write(prologue[x - 2] + "\n")
                write(prologue[x - 1] + "\n")
                write(prologue[x])
                write("\n" * y)
            elif (x == 19):
                global level
                level = 1
        except IndexError:
            print("List index out of range!")

    if (data == ">>> ") and (level == 1):     # level 1
        y = 25
        write("Je staat in een kamer. Wat doe je?")
        write("\n"*y)
    write("")

mainloop()