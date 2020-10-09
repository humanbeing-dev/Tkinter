from tkinter import *
# from PIL import ImageTk, Image
import requests
import json
import datetime

root = Tk()
root.title("Weather App")
# root.iconbitmap("logo.ico")
root.geometry("250x250")

api_key = "45f192d822feba4152c52f9eb28aeb9c"
city_name = "Warsaw"
units = StringVar()
units.set('metric')
unit_options = ['standard', 'metric', 'imperial']
lang = StringVar()
lang.set('en')
lang_options = ['en', 'pl', 'de']


def get_weather(units, lang, *args):

    try:
        your_city = args[0]
    except:
        your_city = root.children['city'].get()

    units = units.get()
    lang = lang.get()
    api_request = requests.get(f"""
        http://api.openweathermap.org/data/2.5/weather?q={your_city}&appid={api_key}&units={units}&lang={lang}""")

    api = api_request.json()
    weather_data = f"""
        Miasto: {api['name']}
        Opis pogody: {api['weather'][0]['description']}
        Temperatura: {api['main']['temp']} {chr(176)}C
        Odczuwalna: {api['main']['feels_like']} {chr(176)}C
        Minimalna: {api['main']['temp_min']} {chr(176)}C
        Maksymalna: {api['main']['temp_max']} {chr(176)}C
        Godzina pomiaru: {datetime.datetime.fromtimestamp(api['dt']).strftime("%H:%M:%S")}
        Wschod: {datetime.datetime.fromtimestamp(api['sys']['sunrise']).strftime("%H:%M:%S")}
        Zachod: {datetime.datetime.fromtimestamp(api['sys']['sunset']).strftime("%H:%M:%S")}
    """

    lbl = Label(root, text=weather_data, anchor=W)
    lbl.grid(row=3, column=0, columnspan=3, stick=E+W+N+S)


lbl = Label(root, text="Your city: ", width=10).grid(row=0, column=0)
box = Entry(root, width=10, name="city").grid(row=0, column=1)
btn = Button(root, text="Search", width=20, command=lambda units=units, lang=lang: get_weather(units, lang)).grid(row=1, column=0, columnspan=2)
drp1 = OptionMenu(root, units, *unit_options)
drp1.config(width=8)
drp1.grid(row=0, column=2, columnspan=2)
drp2 = OptionMenu(root, lang, *lang_options)
drp2.config(width=8)
drp2.grid(row=1, column=2, columnspan=2)
btn_city = Button(root, text="Warsaw", width=30,
                  command=lambda units=units, lang=lang, city="Warsaw": get_weather(units, lang, city))
btn_city.grid(row=2, column=0, columnspan=3)



root.mainloop()
