from main import *

def player():
    try:
        write("Name: " + (doc['all']['characters']['player_0']['name']))
        write("Health: " + (doc['all']['characters']['player_0']['health']))
        write("Energy: " + (doc['all']['characters']['player_0']['energy']))
        write("Moneyz: " + (doc['all']['characters']['player_0']['moneyz']))
        write("Inventory:")
        write((doc['all']['characters']['player_0']['inventory']['item_0']))
        write((doc['all']['characters']['player_0']['inventory']['item_1']))
        write((doc['all']['characters']['player_0']['inventory']['item_2']))
        write((doc['all']['characters']['player_0']['inventory']['item_3']))
        write((doc['all']['characters']['player_0']['inventory']['item_4']))
    except KeyError:
        return("")
    return("")