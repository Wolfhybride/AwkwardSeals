from main import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

def defeat1():

    print("Hier heb je je Final Assingment 2")
    print("*Je hebt final Assingment 2 verkregen!")

def defeat2():
    print("Oké oké ik ga al")
    print("*Je hebt final Assingment 3 verkregen!*")

def defeat3():
    print("Wat een geluksvogel ben je ook. Uit goeie wil geef ik je een final Assignment")
    print("*Je hebt final Assignment 4 gekregen*")

def defeat4():
    print("Oké oké ik ga al weg.. Sla me niet aub! Hier heb je Final Assignment 5")
    print("Je hebt Final Assignment 5 gekregen!")

def defeat5():
    print("*You have won*")
    print("*Je hebt final assignment 6 verkregen!")

def defeat6():
    print("*Student1 rent weg en laat uit paniek zijn laptop liggen met het document open. Je mailt het naar jezelf*")
    print("*Je hebt final assignment 7 verkregen!")

def defeat7():
    print("Uit schaamte zal ik je toegang geven tot deze verdieping. Je kan Bart op het dak vinden.")
    print("* Je hebt final assignment 8 verkregen!")

def choose(choice):                                         #raw data that write(string) prints to the screen as text
   mainWindow.delete(0, END)
   if (choice == ">>> 1"):
       write("You used Huiswerk inleveren")
   elif (choice == ">>> 2"):
       write("You used Slimme vragen stellen")
   elif (choice == ">>> 3"):
           write("You used Blackmail")
   elif (choice == ">>> 4"):
               write("You used Kopstoot")
   else:
        write("")

#startScreenfunction()

mainloop()
