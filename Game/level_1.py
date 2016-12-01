from main2 import *

prologue = []

for line in doc["root"]["level_1"]["prologue"]:
    prologue.append(doc["root"]["level_1"]["prologue"][line])

for line in prologue:
    print(line)