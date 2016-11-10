from main import *
from studentLifeASCII import studentLife
from Player_0 import player

#write((studentLife()))

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    #print(data)
    #write(data)
    choose(data)
    return data

console.bind('<Return>', return_entry)

def clearScreen():
    write("""
        \n
        \n
        \n
        \n
        \n
        \n
        \n
        \n
        \n
        \n
        \n

    """)
    return ("")

def choose(choice):                                         #raw data that write(string) prints to the screen as text
    write("""
        \n
        \n
        \n
        \n
        \n
        \n
        \n
    """)
    if choice == ">>> 1":
        write("\n")
        write("You typed in number one!")
        write("""
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n



        """)
        #mainWindow.del(choice)
    elif choice == ">>> 2":
        write((studentLife()))
        write("""
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
        """)
    elif choice == ">>> 3":
        write((player()))
        write("""
            \n
            \n
            \n
            \n
            \n
            \n
            \n
        """)
    elif choice == ">>> 4":
        write("Exterminate, exterminate!")
        write("""
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n

        """)
        #raise SystemExit
    elif choice == ">>> clear":
        clearScreen()
    elif choice == ">>> map":
        write("\n\n")
        write("       " + str(doc['all']['ascii']['map']['map_8']))
        write("\n")
    else:
        #write("\n")
        write("You can only fill in numbers 1 to 3.\n     - 4 Terminates the program.\n     - map prints the map.\n     - clear clears the screen.")
        write("""
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n
            \n

        """)
    write("")

mainloop()