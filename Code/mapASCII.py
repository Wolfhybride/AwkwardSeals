import xmltodict
#import time
#from main import *

with open("file.xml") as fd:
    doc = xmltodict.parse(fd.read())

#write(doc['all']['ascii']['map'])
print(doc['all']['ascii']['map'])