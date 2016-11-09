from main import *
from studentLifeASCII import studentLife
from Player_0 import player
#write(".........")
write((studentLife()))

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    #print(data)
    #write(data)
    choose(data)
    return data

console.bind('<Return>', return_entry)

def choose(choice):                                         #raw data that write(string) prints to the screen as text
    #write("     Output >>> ")
    write("\n")
    if choice == ">>> 1":
        write("You typed in number one!")
    elif choice == ">>> 2":
        write((studentLife()))
    elif choice == ">>> 3":
        write((player()))
    elif choice == ">>> 4":
        raise SystemExit
    else:
        write("You can only fill in numbers 1 to 4.\n     4 Terminates the program.")
    write("")

mainloop()