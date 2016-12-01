from main import *

def return_entry(data):                                   #gets input and returns it
    data = console.get()
    console.delete(0, END)
    console.insert(0, string = ">>> ")
    choose(data)
    return data

console.bind('<Return>', return_entry)

def start1():
    write("")
    write("A BATTLE OCCURS!")
    write("The student can't attack! Quickly, destroy your enemy!")
    write("")
    write("Your attacks include:")
    write("")
    write("Huiswerk inleveren (1)                   Slimme vragen stellen (2)")
    write("Blackmail(3)                             Kopstoot(4)")
    write("")
    return ""

def defeat1():

    write("Hier heb je je Final Assingment 2")
    write("")
    write("*Je hebt final Assingment 2 verkregen!")
    write("")
    write("Level 1 Cleared!")
    return ""

def defeat2():
    write("Oké oké ik ga al")
    write("*Je hebt final Assingment 3 verkregen!*")
    return ""

def defeat3():
    write("Student: Wat een geluksvogel ben je ook. Uit goeie wil geef ik je een final Assignment")
    write("*Je hebt final Assignment 4 gekregen*")
    return ""

def defeat4():
    write("Oké oké ik ga al weg.. Sla me niet aub! Hier heb je Final Assignment 5")
    write("Je hebt Final Assignment 5 gekregen!")
    return ""

def defeat5():
    write("*You have won*")
    write("*Je hebt final assignment 6 verkregen!")
    return ""

def defeat6():
    write("*Student1 rent weg en laat uit paniek zijn laptop liggen met het document open. Je mailt het naar jezelf*")
    write("*Je hebt final assignment 7 verkregen!")
    return ""

def defeat7():
    write("Student: Uit schaamte zal ik je toegang geven tot deze verdieping. Je kan Bart op het dak vinden.")
    write("* Je hebt final assignment 8 verkregen!")
    return ""

health_Player = 15
health_Student1 = 5

def choose(choice):                                         #raw data that write(string) prints to the screen as text
   mainWindow.delete(0, END)
   if health_Player <= 0:
    write("You are DEAD!")

   elif health_Student1 <= 0:
     write("You are VICTORIOUS!")
     write(str(defeat1()))

   elif (choice == ">>> 1"):
     write("You used Huiswerk inleveren")
     global health_Student1
     health_Student1 -= 1
     write("Student HP: " + str(health_Student1) + "\n")

   elif (choice == ">>> 2"):
    write("You used Slimme vragen stellen")
    global health_Student1
    health_Student1 -= 1
    write("Student HP: " + str(health_Student1) + "\n")

   elif (choice == ">>> 3"):
    write("You used Blackmail")
    global health_Student1
    health_Student1 -= 2
    write("Student HP: " + str(health_Student1) + "\n")

   elif (choice == ">>> 4"):
    write("You used Kopstoot")
    global health_Student1
    health_Student1 -= 2.5
    write("Student HP: " + str(health_Student1) + "\n")

#startScreenfunction()
start1()
mainloop()