import xmltodict
import time

with open("file.xml") as fd:
    doc = xmltodict.parse(fd.read())

#for key in (doc['all']['characters']['player_0']):
#    print("{:6}".format(key),":","{:15}".format((doc['all']['characters']['player_0'])[key]))
#    time.sleep(0.3)

def name():
    print(" Name:","{:6}".format(doc['all']['characters']['player_0']['name']))
def health():
    print(" Health:","{:6}".format(doc['all']['characters']['player_0']['health']))
def energy():
    print(" Energy:","{:6}".format(doc['all']['characters']['player_0']['energy']))
def moneyz():
    print(" Moneyz:","{:6}".format(doc['all']['characters']['player_0']['moneyz']))
def inventory():
    print(" Inventory:\n" + "{:6}".format((doc['all']['characters']['player_0']['inventory'])))
name()
time.sleep(.3)
health()
time.sleep(.3)
energy()
time.sleep(.3)
moneyz()
time.sleep(.3)
print("")
inventory()
