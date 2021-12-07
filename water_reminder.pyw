import time

from plyer import notification #pip install plyer

import pyttsx3



engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('rate', 180) # if you want to set speaking speed 

# engine.setProperty('voice','voices[1].id') for female voice 

engine.runAndWait()



def speak(audio):

    engine.say(audio)

    engine.runAndWait() 



if __name__ == "__main__":

    while True: 

     speak ('Please drink water now!!!')

     speak ('GO!!')

     notification.notify(

        title = "Please Drink Water Now",

        message = '''Bhai jaa pele pani

Good for ur body''', 

        timeout= 10,

        app_icon = (r"C:\Users\Invisible\Desktop\Beyond_class_Time\Iconsmind-Outline-Glass-Water.ico")

    ) 

     time.sleep(60*60)