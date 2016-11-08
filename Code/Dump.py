#import xmltodict

#with open("file.xml") as fd:
#    doc = xmltodict.parse(fd.read())

#(doc['all']['player']['@has']) = "Player3"
#print(doc['all']['player']['@has']) # == u'an attribute'
#print(doc['all']['player']['playername'])
#(doc['all']['player']['playername']) = input("Voer een naam in: ")
#print(doc['all']['player']['playername'])
#print(doc['all']['ascii']['map1'])
#print(doc['all']['ascii'])
#print(*doc['mydocument']['and']['many']) # == [u'elements', u'more elements']
#print(doc['mydocument']['plus']['@a']) # == u'complex'
#print(doc['mydocument']['plus']['#text']) # == u'element as well'


#def toonVenster():
#    label = Label(master=root,
#    text="Dinges" + str(playerName()),
#    background='black',
#    foreground='white',
#    font=('Arial', 10, 'bold italic'),
#    width=30,
#    height=5)
#    label.pack()

#def toonVenster2():
#    label = Label(master=root,
#    text='Je valt opeens dood',
#    background='black',
#    foreground='white',
#    font=('Arial', 10, 'bold italic'),
#    width=30,
#    height=5)
#    label.pack()

#def toonVenster3():
#    label = Label(master=root,
#    text='Je ziet een lichtje',
#    background='black',
#    foreground='white',
#    font=('Arial', 10, 'bold italic'),
#    width=30,
#    height=5)
#    label.pack()

#def toonVenster4():
#    label = Label(master=root,
#    text='Daaag',
#    background='black',
#    foreground='white',
#    font=('Arial', 10, 'bold italic'),
#    width=30,
#    height=5)
#    label.pack()



import sys
from tkinter import *

sys.path.append("studentLifeASCII.py")

class App(Frame):
    def run_script(self):
        sys.stdout = self
        try:
            del(sys.modules["studentLifeASCII.py"])
        except:
            pass
        import studentLifeASCII
        sys.stdout = sys.__stdout__


    def build_widgets(self):
        self.text1 = Text(self)
        self.text1.pack(side=TOP)
        self.button = Button(self)
        self.button["text"] = "Trigger script"
        self.button["command"] = self.run_script
        self.button.pack(side=TOP)

    def write(self, txt):
        self.text1.insert(INSERT, txt)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.build_widgets()

root = Tk()
app = App(master = root)

app.mainloop()
