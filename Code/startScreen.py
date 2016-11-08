import xmltodict
from tkinter import *
import time



with open("file.xml") as fd:
    doc = xmltodict.parse(fd.read())

root = Tk()

def studentLifeASCII():
    print(
        "  " + str(doc['all']['ascii']['studentLife_0'])
    )
    time.sleep(0.5)
    print(
        "  " + str(doc['all']['ascii']['studentLife_1'])
    )
    time.sleep(0.5)
    print(
        "  " + str(doc['all']['ascii']['studentLife_2'])
    )
    time.sleep(0.5)
    print(
        "  " + str(doc['all']['ascii']['studentLife_3'])
    )
    time.sleep(0.5)
    print(
        "  " + str(doc['all']['ascii']['studentLife_4'])
    )
    time.sleep(0.5)
    print(
        "  " + str(doc['all']['ascii']['studentLife_5'])
    )
    time.sleep(0.5)

#studentLifeASCII()

label = LabelFrame(master = root,
            background = 'black',
            text = (studentLifeASCII()),
            justify = 'left',
            font = ("Ariel", 10),
            foreground = 'white',
            height = 30,
            width = 100)

print(label)

root.mainloop()