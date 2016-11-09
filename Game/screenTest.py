from main import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    print(data)
    #write(data)
    choose(data)
    return data

console.bind('<Return>', return_entry)

def choose(choice):                                         #raw data that write(string) prints to the screen as text
    write("Input >>> " + str(choice))
    write("Output >>> ")
    if choice == "1":
        write("You typed in number one!")
    elif choice == "2":
        import studentLifeASCII
    elif choice == "3":
        write(" Name: "+" {:6}".format(doc['all']['characters']['player_0']['name']))
        write(" Health: "+ " {:6}".format(doc['all']['characters']['player_0']['health']))
        write(" Energy: "+ " {:6}".format(doc['all']['characters']['player_0']['energy']))
        write(" Moneyz: "+ " {:6}".format(doc['all']['characters']['player_0']['moneyz']))
        write(" Inventory:\n" + "{:6}".format((doc['all']['characters']['player_0']['inventory'])))
    elif choice == "4":
        root.destroy()
    else:
        write("You can only fill in numbers 1 to 4. 4 Terminates the program.")
    write("")

mainloop()