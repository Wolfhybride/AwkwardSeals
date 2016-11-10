import xmltodict
import time

with open("verdieping2.xml") as fd:
    doc = xmltodict.parse(fd.read())

#for key in (doc['all']['characters']['player_0']):
#    print("{:6}".format(key),":","{:15}".format((doc['all']['characters']['player_0'])[key]))
#    time.sleep(0.3)


def koffietext2():
    print((doc['all']['levels']['floor2_koffie']['dialoog']['koffietext2']))

def lifttext2():
     print(doc['all']['levels']['floor2_lift']['dialoog']['lifttext2'])


def studenttext2():
    print((doc['all']['levels']['floor2_student']['dialoog']['studenttext2']))

def battletext2():
    battle2 = doc['all']['levels']['floor2_battle']['dialoog']['battletext2']
    print("\n".join(battle2))

koffietext2()
print("\n")
lifttext2()
print("\n")
studenttext2()
print("\n")
battletext2()
