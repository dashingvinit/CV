from tkinter import *
from tkinter import font
from numpy import imag
import requests
import json
from datetime import datetime

# Initialize Window

root = Tk()
root.geometry("800x500")  # size of the window by default
root.resizable(0, 0)  # to make the window size fixed
# title of our window
root.title("Weather Forecasting App - Vinit Uid-21BCS7277 ")
root.iconbitmap()
# Define Img
bg = PhotoImage(
    file="C:/Users/VinitKumarParakh/Desktop/CU B.tech/IR/Python App/osman-rana-HOtPD7Z_74s-unsplash.png") // change it !!
# Create Lable
my_lable = Label(root, image=bg)
my_lable.place(x=0, y=0, relwidth=1, relheight=1)

# ----------------------Functions to fetch and display weather info
city_value = StringVar()


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_value = StringVar()


def showWeather():
    # Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "69f4c58a57d53bf1dbbf26296ff387cd"  # sample API

    # Get city name from user from the input field (later in the code)
    city_name = city_value.get()

    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
        city_name + '&appid='+api_key

    # Get the response from fetched url
    response = requests.get(weather_url)

    # changing response from json to python readable
    weather_info = response.json()

    tfield.delete("1.0", "end")  # to clear the text field for every new output

# as per API documentation, if the cod is 200, it means that weather data was successfully fetched

    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

# -----------Storing the fetched values of weather of a city

        # converting default kelvin value to Celcius
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

# assigning Values to our weather varaible, to display as output

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    # to insert or send value in our Text Field to display output
    tfield.insert(INSERT, weather)


# ------------------------------Frontend part of code - Interface


city_head = Label(root, text='Entre City Name', font='arial', background="lightblue").pack(
    pady=10)  # to generate label heading

inp_city = Entry(root, textvariable=city_value,
                 width=18, font='arial', bg="#CC7722").pack()


Button(root, command=showWeather, text="Check Weather", font="arial",
       bg='lightblue', fg='black', activebackground="teal", padx=8, pady=8).pack(pady=20)

# to show output

weather_now = Label(root, text="The Weather is :",
                    font='arial').pack(pady=10)

tfield = Text(root, width=60, height=10, bg="#CC7722")
tfield.pack()

root.mainloop()

