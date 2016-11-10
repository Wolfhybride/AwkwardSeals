import xmltodict
import time

with open("intro.xml") as fd:
    doc = xmltodict.parse(fd.read())

def prologue():
    prologue = ((doc['all']['levels']['prologue']['dialoog']['text_prologue']))
    print("\n".join(prologue))

def intro():
    intro = ((doc['all']['levels']['intro']['dialoog']['intro_text']))
    print("\n".join(intro))

prologue()
print("\n")
intro()
