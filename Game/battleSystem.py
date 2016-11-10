from main import *

inventory = []

name = (doc['all']['characters']['player_0']['name'])
print(name)
health = (doc['all']['characters']['player_0']['health'])
print(health)

derp = int(health) + 1
print(derp)

energy = (doc['all']['characters']['player_0']['energy'])
print(energy)
moneyz = (doc['all']['characters']['player_0']['moneyz'])
print(moneyz)
try:
    inventory.append(doc['all']['characters']['player_0']['inventory']['item_0'])
    inventory.append(doc['all']['characters']['player_0']['inventory']['item_1'])
    inventory.append(doc['all']['characters']['player_0']['inventory']['item_2'])
    inventory.append(doc['all']['characters']['player_0']['inventory']['item_3'])
    inventory.append(doc['all']['characters']['player_0']['inventory']['item_4'])
    inventory.append(doc['all']['characters']['player_0']['inventory']['item_5'])
    print(*inventory,sep="\n")
except KeyError:
    print(*inventory,sep="\n")