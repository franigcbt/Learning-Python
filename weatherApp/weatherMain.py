from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
import json

url = 'http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}'
url2 = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def search():
    city = city_text.get()
    weather = getCity(city)

    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        statusImage['file'] = 'icons/{}.png'.format(weather[3])
        temp_lbl['text'] = '{:.1f}° C'.format(weather[2])
        weather_lbl['text'] = weather[4]
    else:
        print('city not found')
        #messagebox.showerror('Error', 'Cannot find city {}'.format(city))

def getCity(city):
    #Call GEO API for get the lattitude and longitude by city name input
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        #lat, lon
        lat = json[0]['lat']
        lon = json[0]['lon']
            #print(result.content)
         #if request succeded format lat & lon into second request
        final = requests.get(url2.format(lat, lon, api_key))

       
        if final:
            #JSON 2 VARIABLE IS WEATHER INFORMATION
            json2 = final.json()
            currentCity = json2['name']
            country = json2['sys']['country']
            temp_kelvin = json2['main']['temp']
            temp_celcius = temp_kelvin - 273.15
            icon = json2['weather'][0]['icon']
            weather = json2['weather'][0]['main']


            finalReturn = (currentCity, country, temp_celcius, icon, weather)
            print(finalReturn)
            return finalReturn
    else:
        print('not found')


getCity('Buenos Aires')

app = Tk()
app.title('Minimal Weather App')
app.geometry('390x525')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn=Button(app, text='Search', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font = ('normal', 15))
location_lbl.pack()

statusImage = PhotoImage(file='')
images = Label(app, image=statusImage)
images.pack()

temp_lbl = Label(app, text='', font=('bold', 20))
temp_lbl.pack()

weather_lbl = Label(app, text='', font = ('normal', 15))
weather_lbl.pack()




app.mainloop()