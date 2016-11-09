import xmltodict
import time
from main import *

with open("file.xml") as fd:
    doc = xmltodict.parse(fd.read())

def studentLifeASCII():
    write(
        "    " + str(doc['all']['ascii']['studentLife_0'])
    )
    time.sleep(0.3)
    write(
        "   " + str(doc['all']['ascii']['studentLife_1'])
    )
    time.sleep(0.3)
    write(
        "  " + str(doc['all']['ascii']['studentLife_2'])
    )
    time.sleep(0.3)
    write(
        "   " + str(doc['all']['ascii']['studentLife_3'])
    )
    time.sleep(0.3)
    write(
        "   " + str(doc['all']['ascii']['studentLife_4'])
    )
    time.sleep(0.3)
    write(
        "  " + str(doc['all']['ascii']['studentLife_5'])
    )
    time.sleep(0.3)
studentLifeASCII()
