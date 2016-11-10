import xmltodict
import time

with open("verdieping3.xml") as fd:
    doc = xmltodict.parse(fd.read())


def koffietext3():
    print((doc['all']['levels']['floor3_koffie']['dialoog']['koffietext3']))

def lifttext3():
    print((doc['all']['levels']['floor3_lift']['dialoog']['lifttext3']))


def studenttext3():
    studenttext3 = ((doc['all']['levels']['floor3_student']['dialoog']['studenttext3']))
    print("\n".join(studenttext3))


def battletext3():
   battletext3 = ((doc['all']['levels']['floor3_battle']['dialoog']['battletext3']))
   print("\n".join(battletext3))

koffietext3()
print("\n")
lifttext3()
print("\n")
studenttext3()
print("\n")
battletext3()
