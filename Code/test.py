from main import *

with open("test.xml") as fd:
    doc = xmltodict.parse(fd.read())

def bartdialog():
   bart = ((doc['all']['levels']['level1_bart']['dialoog']['barttext1']))
   write("\n".join(bart))

def koffietext1():
    write((doc['all']['levels']['level1_koffie']['dialoog']['koffietext1']))

def lifttext1():
    lift1 = ((doc['all']['levels']['level1_lift']['dialoog']['lifttext1']))
    write("\n".join(lift1))

def studenttext():
    studenttext1 = ((doc['all']['levels']['level1_student']['dialoog']['studenttext1']))
    write("\n".join(studenttext1))

