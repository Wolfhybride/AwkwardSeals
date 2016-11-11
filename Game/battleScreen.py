from main import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

def start1():
    write("PLAYER 1, BATTLE STARTS")

def defeat1():

    write("Hier heb je je Final Assingment 2")
    write("*Je hebt final Assingment 2 verkregen!")

def defeat2():
    write("Oké oké ik ga al")
    write("*Je hebt final Assingment 3 verkregen!*")

def defeat3():
    write("Wat een geluksvogel ben je ook. Uit goeie wil geef ik je een final Assignment")
    write("*Je hebt final Assignment 4 gekregen*")

def defeat4():
    write("Oké oké ik ga al weg.. Sla me niet aub! Hier heb je Final Assignment 5")
    write("Je hebt Final Assignment 5 gekregen!")

def defeat5():
    write("*You have won*")
    write("*Je hebt final assignment 6 verkregen!")

def defeat6():
    write("*Student1 rent weg en laat uit paniek zijn laptop liggen met het document open. Je mailt het naar jezelf*")
    write("*Je hebt final assignment 7 verkregen!")

def defeat7():
    write("Uit schaamte zal ik je toegang geven tot deze verdieping. Je kan Bart op het dak vinden.")
    write("* Je hebt final assignment 8 verkregen!")

health_Player = 15
health_Student1 = 5

def choose(choice):                                         #raw data that write(string) prints to the screen as text
   mainWindow.delete(0, END)
   if health_Player <= 0:
    write("You are DEAD!")

   elif health_Student1 <= 0:
     write("You are VICTORIOUS!")
     write(defeat1())


   elif (choice == ">>> 1"):
     write("You used Huiswerk inleveren")
     global health_Student1
     health_Student1 -= 1
     write(str(health_Student1))
   elif (choice == ">>> 2"):
    write("You used Slimme vragen stellen")
    global health_Student1
    health_Student1 -= 1
    write(str(health_Student1))
   elif (choice == ">>> 3"):
    write("You used Blackmail")
    global health_Student1
    health_Student1 -= 2
    write(str(health_Student1))
   elif (choice == ">>> 4"):
    write("You used Kopstoot")
    global health_Student1
    health_Student1 -= 2.5
    write(str(health_Student1))



#startScreenfunction()
start1()
mainloop()
