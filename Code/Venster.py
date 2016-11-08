from tkinter import *
import xmltodict
import time
import os

root = Tk()

with open("file.xml") as fd:
    doc = xmltodict.parse(fd.read())

def studentLifeASCII():
    print(
        "  " + str(doc['all']['ascii']['studentLife_0'])
    )
    time.sleep(0.5)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_1'])
    )
    time.sleep(0.5)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_2'])
    )
    time.sleep(0.5)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_3'])
    )
    time.sleep(0.5)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_4'])
    )
    time.sleep(0.5)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_5'])
    )
    time.sleep(0.5)

label = Label(master = root,
        background = 'black',
        text = (studentLifeASCII()),
        justify = 'left',
        font = ("Courier", 10),
        foreground = 'white',
        height = 30,
        width = 100)
label.pack()

def additem():

    b.configure(text=(studentLifeASCII()))

items = 14
b = Button(root, text="I have %s items" % (items), command=additem)
b.pack()

root.mainloop()