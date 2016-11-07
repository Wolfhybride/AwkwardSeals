from tkinter import *

def toonVenster():
    label = Label(master=root,
    text='Nini staat er',
    background='black',
    foreground='white',
    font=('Arial', 10, 'bold italic'),
    width=30,
    height=5)
    label.pack()

def toonVenster2():
    label = Label(master=root,
    text='Je valt opeens dood',
    background='black',
    foreground='white',
    font=('Arial', 10, 'bold italic'),
    width=30,
    height=5)
    label.pack()

def toonVenster3():
    label = Label(master=root,
    text='Je ziet een lichtje',
    background='black',
    foreground='white',
    font=('Arial', 10, 'bold italic'),
    width=30,
    height=5)
    label.pack()

def toonVenster4():
    label = Label(master=root,
    text='Daaag',
    background='black',
    foreground='white',
    font=('Arial', 10, 'bold italic'),
    width=30,
    height=5)
    label.pack()

root = Tk()


background_image = PhotoImage(file="test1.gif")

label = Label(master=root,
            background='black',
            text='Je bent in een kamer',
            foreground='white',
            height = 5,
            width = 30)
label.pack()

linkerframe = Frame(master=root)
linkerframe.pack(side=LEFT)

rechterframe = Frame(master=root)
rechterframe.pack(side=RIGHT)


button1 = Button(master=linkerframe, text='Open de deur', command = toonVenster)
button1.pack(side = TOP, pady=10)

button2 = Button(master=linkerframe, text='Doorzoek de kast', command = toonVenster2)
button2.pack(side=BOTTOM, pady=10)

button3 = Button(master=rechterframe, text='Ga naar beneden', command = toonVenster3)
button3.pack(side = TOP, pady=10)

button4 = Button(master=rechterframe, text='Ga terug', command = toonVenster4)
button4.pack(side=BOTTOM, pady=10)

root.mainloop()
