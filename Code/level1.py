import xmltodict
import time

with open("test.xml") as fd:
    doc = xmltodict.parse(fd.read())

#for key in (doc['all']['characters']['player_0']):
#    print("{:6}".format(key),":","{:15}".format((doc['all']['characters']['player_0'])[key]))
#    time.sleep(0.3)

#def bartdialog():
#   bart = ((doc['all']['levels']['level']['dialoog']['barttext1']))
#   print("\n".join(bart))

#def koffietext1():
#    print((doc['all']['levels']['level1_koffie']['dialoog']['koffietext1']))

#def lifttext1():
#    lift1 = ((doc['all']['levels']['level1_lift']['dialoog']['lifttext1']))
#    print("\n".join(lift1))

def studenttext():
    studenttext1 = ((doc['all']['levels']['level1_student']['dialoog']['studenttext1']))
    print("\n".join(studenttext1))

studenttext()
