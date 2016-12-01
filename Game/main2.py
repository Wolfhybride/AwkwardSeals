from tkinter import *
import xmltodict

with open("xml.xml") as fd:
    doc = xmltodict.parse(fd.read())

root = Tk()
root.title("Student Life")
root.resizable(width=False, height=False)

mainWindow = Text(
    root,
    height = 30,
    width = 100,
    background = ('black'),
    foreground = ('white'),
    font = ('Courier',10,'bold'),
    cursor = 'plus',
    state = 'disable',
    wrap = WORD,
)
mainWindow.pack(anchor = 'n', side = 'top')
mainWindow.winfo_geometry()

#dialogueWindow = Text(
#    mainWindow,
#    height = 30,
#    width = 100,
#    background = ('black'),
#    foreground = ('white'),
#    font = ('Courier', 10, 'bold'),
#    cursor = 'plus',
#    state = 'disable',
#    wrap = WORD,
#    bd = 0,
#    highlightthickness = 0,
#)
#dialogueWindow.pack(anchor = 'n', side = 'top')

def write(string):                                          #print stuff to screen as text
    mainWindow.config(state='normal')
    mainWindow.insert("end", "     " + string + "\n")
    mainWindow.see("end")
    mainWindow.config(state='disable')

console = Entry(root,
                width=100,
                background='#3D3D3D',
                foreground='white',
                #font=('Courier', 10),
                relief='flat',
                borderwidth=0,
                )
console.pack(anchor = 'center',
             #fill = 'both',
             side = 'bottom'
             )
console.insert(0,">>> ")