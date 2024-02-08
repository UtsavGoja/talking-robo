import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 110)
engine.say("Welcome to RoboSpeaker, Created by Utsav Goja")
engine.runAndWait()

while True:
    x = input("Enter what you want me to speak: ")
    if x == "q":
        engine.say("Thank you for using me, ta ta byebye")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()