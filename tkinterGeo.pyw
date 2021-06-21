from tkinter import *
import tkinter.font as tkFont
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import time
from tzwhere import tzwhere
import pytz
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from geopy import geocoders




t = Tk()
t.configure(bg='black')
t.config(width=600,height=300)
fontStyle = tkFont.Font(family="Cascadia Code", size=20)
fontButton = tkFont.Font(family="Cascadia Code", size=15)
fontEnd = tkFont.Font(family="Cascadia Code", size=35)

a1 = Label(t, text= "Input your country:", fg="white", bg="black", font=fontStyle)
a1.place(x=0,y=0)

b1 = Entry(t, font=fontButton)
b1.place(x=315, y=10)
b1.configure({"background": "black"})
b1.configure({"foreground": "peach puff"})

a2= Label(t, text="Input city name:", fg="white", bg="black", font=fontStyle)
a2.place(x=0,y=50)

b2 = Entry(t, font=fontButton)
b2.place(x=315, y=55)
b2.configure({"background": "black"})
b2.configure({"foreground": "peach puff"})




def naći():
    owm = OWM('16c05286c9f21ff8944445cacf1ee058')
    mgr = owm.weather_manager()
    asd = b2.get()+", "+b1.get()
    observation = mgr.weather_at_place(asd)
    w = observation.weather
    status = w.detailed_status.capitalize()
    temperature = w.temperature('celsius') 
    avgTemp = temperature['temp']
    stringTemp = str(avgTemp)+"°C"
    wind = str(round((w.wind().get("speed",0)),2))+" km/h wind"
    windStr = str(wind)
    windStr.replace("{km/h wind}", "km/h wind")
    #geolocator = Nominatim(user_agent="pexate")
    #location = geolocator.geocode(b2.get())
    #location.latitude, location.longitude
    #obj = TimezoneFinder()
    #tz = pytz.timezone(obj.timezone_at(lng=location.latitude, lat=location.longitude))
    #test = datetime.now(tz)
    #finTime = str(test.hour-1)+":"+str(test.minute)

    

    a3 = Label(t, text=status, bg="black", fg="gray", font=fontEnd)
    a4 = Label(t, text=status, bg="black", fg="gray", font=fontEnd)
    a5 = Label(t, text=windStr, bg="black", fg="gray", font=fontStyle)
    #a6 = Label(t, text=windStr, bg="black", fg="gray", font=fontStyle)
 
    
    if a3.cget("text") == "Clear sky":
        a3 = Label(t, text=status, bg="black", fg="cyan", font=fontEnd)
        a4 = Label(t, text=stringTemp, bg="black", fg="cyan", font=fontStyle)
        a5 = Label(t, text=windStr, bg="black", fg="cyan", font=fontStyle)
        #a6 = Label(t, text=finTime, bg="black", fg="cyan", font=fontStyle)
     
    
    elif "clouds" in a3.cget("text") or "Cloudy" in a3.cget("text") or "cloud" in a3.cget("text"):
        a3 = Label(t, text=status, bg="black", fg="azure4", font=fontEnd)
        a4 = Label(t, text=stringTemp, bg="black", fg="azure4", font=fontStyle)
        a5 = Label(t, text=windStr, bg="black", fg="azure4", font=fontStyle)
       # a6 = Label(t, text=finTime, bg="black", fg="azure4", font=fontStyle)
      

    
    elif "rainy" in a3.cget("text") or "Rainy" in a3.cget("text") or "rain" in a3.cget("text"):
        a3 = Label(t, text=status, bg="black", fg="dodger blue", font=fontEnd)
        a4 = Label(t, text=stringTemp, bg="black", fg="dodger blue", font=fontStyle)
        a5 = Label(t, text=windStr, bg="black", fg="dodger blue", font=fontStyle)
        #a6 = Label(t, text=finTime, bg="black", fg="dodger blue", font=fontStyle)
       

    
    else:
        a3 = Label(t, text=status, bg="black", fg="white", font=fontEnd)
        a4 = Label(t, text=stringTemp, bg="black", fg="white", font=fontStyle)
        a5 = Label(t, text=windStr, bg="black", fg="white", font=fontStyle)
        #a6 = Label(t, text=finTime, bg="black", fg="white", font=fontStyle)
        

    
    
    a3.place(x=300,y=185, anchor="center")
    a4.place(x=300,y=230, anchor="center")
    a5.place(x=300,y=265, anchor="center")
    #a6.place(x=300,y=300, anchor="center")
    

    temperature = w.temperature('celsius') 
    avgTemp = temperature['temp']


g = Button(t, text="Find current weather", command=naći, bg="black", fg = "white", font=fontButton)
time.sleep(5)
g.place(x=300,y=125, anchor="center")

t.mainloop()