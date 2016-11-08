from tkinter import *
import xmltodict
import time
import os

with open("file.xml") as fd:
    doc = xmltodict.parse(fd.read())

def studentLifeASCII():
    print(
        "  " + str(doc['all']['ascii']['studentLife_0'])
    )
    time.sleep(0.3)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_1'])
    )
    time.sleep(0.3)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_2'])
    )
    time.sleep(0.3)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_3'])
    )
    time.sleep(0.3)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_4'])
    )
    time.sleep(0.3)
    try:
        os.system('cls')
    except OSError:
        os.system('clear')
    print(
        "  " + str(doc['all']['ascii']['studentLife_5'])
    )
    time.sleep(0.3)

studentLifeASCII()
