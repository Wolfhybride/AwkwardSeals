from main2 import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

write("\n")

startInput = []
startOutput = []

prologue = []

for line in doc["root"]["level_1"]["prologue"]:                 #prologue
    prologue.append(doc["root"]["level_1"]["prologue"][line])
for line in doc["root"]["start"]["input"]:                      #input
    startInput.append(doc["root"]["start"]["input"][line])
for line in doc["root"]["start"]["output"]:                     #ouput
    startOutput.append(doc["root"]["start"]["output"][line])

write(doc["root"]["start"]["screen"])
write("\n"*3)

def choose(data):                                         #raw data that write(string) writes to the screen as text
    #if data not in startInput[0] and data not in startInput[1] and data not in startInput[2]:
    #    write(doc["root"]["start"]["screen"])
    #    write("")
    #    write(">>> This is not a valid command!")
    #    write("")
    if (data in startInput[0]):  # Start
        write(doc["root"]["start"]["screen"])
        write("")
        write(str(startOutput[0]))
        write("")
        global level
        level = 1
        global x
        x = 0
        for line in prologue:
            write(line)
        x += 1
    elif (data in startInput[1]):  # Settings
        write(str(startOutput[1]))
    elif (data in startInput[2]):  # Stop
        write(str(startOutput[2]))
    elif (data in startInput[3]):  # help
        write(str(startOutput[3]))

    elif (data == ">>> help"):
        write(">>> You choose: help!")
    write("")

mainloop()